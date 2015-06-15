import numpy as np
import contextlib
import math

palette = np.zeros(256)

for i in range(len(palette)):
    r = round((i >> 5) * 36.4)
    g = round(((i >> 2) & 0b111) * 36.4)
    b = (i & 0b11) * 85

    palette[i] = (r << 16) | (g << 8) | b


if __name__ == "__main__":
    print("palette:")
    print(np.vectorize("%x".__mod__)(palette))

