import sys

import numpy as np
import pandas as pd

from skimage.io import imread


def measure_area(arr, target=1, dx=1):
    n_pixels = np.sum(arr == target)
    area = (dx ** 2) * n_pixels
    return area


if __name__ == "__main__":
    filenames = sys.argv[1:]
    names = []
    areas = []
    for fn in filenames:
        name = fn.split(".")[0]
        arr = imread(fn, as_gray=True)
        area = measure_area(arr)
        names.append(name)
        areas.append(area)

    df = pd.DataFrame({"name": names, "area": areas})
    df.to_excel("output/areas.xls")
