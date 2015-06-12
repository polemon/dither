# formulas for this file from:
# http://www.easyrgb.com/index.php?X=MATH

import numpy as np
import contextlib
import math

# Converts sRGB color to CIE's XYZ.
# defaults to white, in order to quickly assert white point in CIE-L*a*b*.
def rgb2xyz(rgb = [255, 255, 255]):
    # normalize gamut
    rgb = np.array(rgb) / 255
    xyz = np.zeros(3)

    # offset calc.
    # linear div. for very small color values.
    for i, c in enumerate(rgb):
        if c > 0.04045:
            rgb[i] = ((c + 0.055) / 1.055)**2.4
        else:
            rgb[i] = c / 12.92

    rgb = np.array(rgb) * 100

    # resultin XYZ color coords.
    # observer: 2°, illuminant: D65
    xyz[0] = rgb[0] * 0.4124 + rgb[1] * 0.3576 + rgb[2] * 0.1805
    xyz[1] = rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722
    xyz[2] = rgb[0] * 0.0193 + rgb[1] * 0.1192 + rgb[2] * 0.9505

    return xyz


# TODO implement
def xyz2rgb(xyz = rgb2xyz()):
    return false


# convert CIE's XYZ to L*a*b*.
# defaults to white.
def xyz2lab(xyz = rgb2xyz()):
    lab = np.zeros(3)
    # observer = 2°, illuminant = D65
    xyz[0] = xyz[0] /  95.047
    xyz[1] = xyz[1] / 100.000
    xyz[2] = xyz[2] / 108.883

    # offset calc.
    # linear div. for very small color values.
    for i, c in enumerate(xyz):
        if c > 0.008856:
            xyz[i] = c**(1/3) # third root
        else:
            xyz[i] = (c * 7.787) + (16/116)

    lab[0] = (116 * xyz[1]) - 16
    lab[1] = 500 * (xyz[0] - xyz[1])
    lab[2] = 200 * (xyz[1] - xyz[2])

    return lab


# TODO implement
def lab2xyz(lab = rgb2lab()):
    return false


def rgb2lab(rgb = [255, 255, 255]):
    return xyz2lab(rgb2xyz(rgb))


def lab2rgb(lab = rgb2lab()):
    return xyz2rgb(lab2xyz(lab))


if __name__ == "__main__":
    print("white 0xFFFFFF")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz()))
    print(np.vectorize("%.3f".__mod__)(rgb2lab()))

    print("red 0xFF000")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([255, 0, 0])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([255, 0, 0])))

    print("green 0x00FF00")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([0, 255, 0])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([0, 255, 0])))

    print("blue 0x0000FF")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([0, 0, 255])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([0, 0, 255])))

    print("yellow 0xFFFF00")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([255, 255, 0])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([255, 255, 0])))
    
    print("magenta 0xFF00FF")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([255, 0, 255])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([255, 0, 255])))
    
    print("cyan 0x00FFFF")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([0, 255, 255])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([0, 255, 255])))

    print("black 0x000000")
    print(np.vectorize("%.3f".__mod__)(rgb2xyz([0, 0, 0])))
    print(np.vectorize("%.3f".__mod__)(rgb2lab([0, 0, 0])))
