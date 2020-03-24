import sys

import numpy as np
import pandas as pd

from skimage.io import imread


def measure_area(arr, target=1, dx=1):
    n_pixels = np.sum(arr == target)
    area = (dx ** 2) * n_pixels
    return area


if __name__ == "__main__":
    dx = float(sys.argv[1])
    filenames = sys.argv[2:]
    names = []
    areas = []
    for fn in filenames:
        name = fn.split(".")[0]
        arr = (imread(fn)[:, :, 3] != 0).astype(int)
        area = measure_area(arr, dx=dx)
        names.append(name)
        areas.append(area)

    df = pd.DataFrame({"name": names, "area": areas})
    df.to_csv("areas.csv")
