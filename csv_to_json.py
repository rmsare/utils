"""
Convert CSV file to GeoJSON
"""

import sys
import csv
import json
import numpy as np

from functools import cmp_to_key
from geojson import Polygon


def sanitize(x):
    x = sort_cw(x)
    x = list(set(x))
    x.append(x[0])
    return x


def sort_cw(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    c = (np.mean(x), np.mean(y))

    def lt(a, b, center=c):
        ax, ay = a
        bx, by = b
        cx, cy = center

        theta_a = (180 / np.pi) * np.arctan2(ay - cy, ax - cx)
        theta_b = (180 / np.pi) * np.arctan2(by - cy, bx - cx)

        if theta_a < 0:
            theta_a = 360 + theta_a
        if theta_b < 0:
            theta_b = 360 + theta_b

        if theta_a < theta_b:
            return -1
        if theta_a > theta_b:
            return 1
        else:
            return 0

    return sorted(points, key=cmp_to_key(lt))


def main():
    infilename = sys.argv[1]
    outfilename = sys.argv[2]

    points = []
    with open(infilename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for lat, lon in reader:
            points.append((float(lon), float(lat)))

    points = sanitize(points)
    poly = Polygon([points])

    with open(outfilename, 'w') as f:
        json.dump(poly, f)


if __name__ == "__main__":
    main()
