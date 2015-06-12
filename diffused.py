import numpy as np
import contextlib
import math

floyd = [ [0, -1, 7],
          [3,  5, 1] ]
floyd = np.matrix(floyd) / 16

false_floyd = [ [-1, 3],
                [ 3, 2] ]
false_floyd = np.matrix(false_floyd) / 8

atkinson = [ [0, -1, 1, 1],
             [1,  1, 1, 0],
             [0,  1, 0, 0] ]
atkinson = np.matrix(atkinson) / 8

jjn = [ [0, 0, -1, 7, 5],
        [3, 5,  7, 5, 3],
        [1, 3,  5, 3, 1] ]
jjn = np.matrix(jjn) / 48


stucki = [ [0, 0, -1, 8, 4],
           [2, 4,  8, 4, 2],
           [1, 2,  4, 2, 1] ]
stucki = np.matrix(stucki) / 42


burkes = [ [0, 0, -1, 8, 4],
           [2, 4,  8, 4, 2] ]
burkes = np.matrix(burkes) / 32

sierra3 = [ [0, 0, -1, 5, 3],
            [2, 4,  5, 4, 2],
            [0, 2,  3, 2, 0] ]
sierra3 = np.matrix(sierra3) / 32

sierra2 = [ [0, 0, -1, 4, 3],
            [1, 2,  3, 2, 1] ]
sierra2 = np.matrix(sierra2) / 16

sierra2_4 = [ [0, -1, 2],
              [1,  1, 0] ]
sierra2_4 = np.matrix(sierra2_4) / 4

stevenson_arce = [ [0,  0,  0, -1,  0, 32, 0],
                   [0, 12,  0, 26,  0, 12, 0],
                   [5,  0, 12,  0, 12,  0, 5] ]
stevenson_arce = np.matrix(stevenson_arce) / 200

if __name__ == "__main__":
    print(__file__)

    print("floyd:")
    print(np.vectorize("%3f".__mod__)(floyd))
    print("false_floyd:")
    print(np.vectorize("%3f".__mod__)(false_floyd))
    print("atkinson:")
    print(np.vectorize("%3f".__mod__)(atkinson))
    print("jjn:")
    print(np.vectorize("%3f".__mod__)(jjn))
    print("stucki:")
    print(np.vectorize("%3f".__mod__)(stucki))
    print("burkes:")
    print(np.vectorize("%3f".__mod__)(burkes))
    print("sierra3:")
    print(np.vectorize("%3f".__mod__)(sierra3))
    print("sierra2:")
    print(np.vectorize("%3f".__mod__)(sierra2))
    print("sierra2_4:")
    print(np.vectorize("%3f".__mod__)(sierra2_4))
    print("stevenson_arce:")
    print(np.vectorize("%3f".__mod__)(stevenson_arce))
