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

#input_file = "day06_input.txt"
#data = np.loadtxt(input_file, delimiter=',', dtype=int)


max_size = data.flatten().max()+1
blank_grid = np.array([[0]*max_size]*max_size)
alphabet = list(map(chr, range(97, 123))) + list(map(chr, range(97-32, 123-32)))


def find_distance(start_x, start_y, finish_x, finish_y):
    return abs(start_x - finish_x) + abs(start_y - finish_y)

# Generate a map for each coordinate


grid_list = []
for start_x,start_y in data:
    grid = blank_grid.copy()
    # grid[x,y] = 0
    for finish_x in range(0, max_size):
        for finish_y in range(0, max_size):
            grid[finish_y, finish_x] = find_distance(start_x, start_y, finish_x, finish_y)
    grid_list.append(grid)

# Compare all maps, assigning winning letter value to lowest numbered cells

labeled_grid = blank_grid.astype(str)
distance_grid = np.array([[max_size*max_size]*max_size]*max_size)
for x in range(0, max_size):
    print("{:.2f}%".format((x/max_size)*100))
    for y in range(0, max_size):
        for i, previous_grid in enumerate(grid_list):
            for j, grid in enumerate(grid_list):
                if alphabet[i] == alphabet[j]:  # Don't compare a grid to itself
                    continue

                logging.info("Grid: {} ({}) Previous: {} ({})".format(alphabet[j],
                                                                      grid[y, x], alphabet[i], previous_grid[y, x]))
                # Compare Grid to "Previous Grid"

                # If Grid has the smaller distance for this cell
                if grid[y, x] < previous_grid[y, x] and grid[y,x] < distance_grid[y, x]:
                    labeled_grid[y, x] = alphabet[j]
                    distance_grid[y, x] = grid[y, x]

                # If Previous Grid has the smaller distance for this cell
                elif previous_grid[y, x] < grid[y, x] and previous_grid[y, x] < distance_grid[y, x]:
                    labeled_grid[y, x] = alphabet[i]
                    distance_grid[y, x] = previous_grid[y, x]

                # If distance is equal
                elif previous_grid[y, x] == grid[y, x] and grid[y, x] <= distance_grid[y, x]:
                    labeled_grid[y, x] = "."
                    distance_grid[y, x] = grid[y, x]

                else:
                    pass

# Throw out letters that touch an edge of the map
disqualified = np.unique([labeled_grid[0], labeled_grid[-1], labeled_grid[:,0], labeled_grid[:,-1]])
for x in range(0, max_size):
    for y in range(0, max_size):
        if labeled_grid[y, x] in disqualified:
            labeled_grid[y, x] = '.'

# Count largest finite area and output

unique, counts = np.unique(labeled_grid, return_counts=True)
letter_counts = dict(zip(unique, counts))
letter_counts.pop('.')
area = max(letter_counts.items(), key=operator.itemgetter(1))

print("Largest Finite Area: {} (Letter {})".format(area[1], area[0]))

# Part Two


