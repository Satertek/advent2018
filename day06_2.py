import numpy as np
import pandas as pd
import logging
import operator

logging.basicConfig(level=logging.WARNING)

test_input = [
    [1, 1],
    [1, 6],
    [8, 3],
    [3, 4],
    [5, 5],
    [8, 9],
    ]
data = np.array(test_input)

input_file = "day06_input.txt"
data = np.loadtxt(input_file, delimiter=',', dtype=int)


max_size = data.flatten().max()+1
blank_grid = np.array([[0]*max_size]*max_size)


def find_distance(start_x, start_y, finish_x, finish_y):
    return abs(start_x - finish_x) + abs(start_y - finish_y)


sum_grid = blank_grid.copy()
for x in range(0, max_size):
    print("{:.2f}%".format((x / max_size) * 100))
    for y in range(0, max_size):
        sum = 0
        for coord_x, coord_y in data:
            sum += find_distance(x,y, coord_x, coord_y) # Sum up distances to all coordinates
            if sum >= 10000:
                sum = 0 # Give up once we break 10k
                break
        sum_grid[y,x] = sum

print("Region Size: {}".format(np.count_nonzero(sum_grid)))