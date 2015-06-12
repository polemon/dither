#########
# ordered.py - ordered dithering algorithms
#
# © 2015 - Szymon 'polemon' Bereziak <polemon@gmail.com>
# License: ISC

import numpy as np
import contextlib
import math

# XXX MOVE TO APPLICABLE FILE!!! XXX
"this is a cluster ditherer, commonly used by newspapers"
news8x8 = [ [24, 10, 12, 26, 35, 47, 49, 37],
            [ 8,  0,  2, 14, 45, 59, 61, 51],
            [22,  6,  4, 16, 43, 57, 63, 53],
            [30, 20, 18, 28, 33, 41, 55, 39],
            [34, 46, 48, 36, 25, 11, 13, 27],
            [44, 58, 60, 50,  9,  1,  3, 15],
            [42, 56, 62, 52, 23,  7,  5, 17],
            [32, 40, 54, 38, 31, 21, 19, 29] ]

bayer2x2 = [ [0, 2],
             [3, 1] ]

bayer3x3 = [ [0, 5, 2],
             [7, 4, 8],
             [3, 6, 1] ]

"this is not exactly a bayer matrix, though"
"it's actually a dispersed matrix using microcluster halftoning"
bayer5x5 = [ [ 0, 14, 22,  5, 16],
             [23,  4, 11, 20,  7],
             [15,  8, 24,  1, 12],
             [ 3, 17, 13,  9, 21],
             [19, 10,  2, 18,  6] ]

def gen_bayer(order = 2):
    # return minimal matrix
    if order == 2:
        return bayer2x2
    elif order == 3:
        return bayer3x3
    elif order == 5:
        return bayer5x5

    # recursive call for larger matrices
    # also, get factor matrix from divisor
    if order % 5 == 0:
        prev_bayer = gen_bayer(int(order / 5))
        factor_m = gen_bayer(5)
    elif order % 3 == 0:
        prev_bayer = gen_bayer(int(order / 3))
        factor_m = gen_bayer(3)
    elif order % 2 == 0:
        prev_bayer = gen_bayer(int(order / 2))
        factor_m = gen_bayer(2)
    else:
        raise ValueError("Order must be multiples of 2, 3, and 5 respectively!")

    # prev order factor
    gen_factor = len(prev_bayer[1])**2
    
    matrix = [ [0 for x in range(order)] for x in range(order) ] 

    # instead of actual dispersion, this uses a more iterative approach
    # factor matrix element times order of previous order matrix, plus previous order element = new element
    for j in range(0, order):
        for i in range(0, order):
            prev_xidx = int(i / len(factor_m[1]))
            prev_yidx = int(j / len(factor_m[1]))

            matrix[j][i] = gen_factor * factor_m[ int(j % len(factor_m[1])) ][ int(i % len(factor_m[1])) ] + prev_bayer[prev_yidx][prev_xidx]

    return matrix

if __name__ == "__main__":
    print(__file__)
    #print(len(bayer2x2[1]))
    print(np.vectorize("%3i".__mod__)(gen_bayer(16)))
