# Advent of Code 2018
# Day 1
# Brian Irelan

import logging

# Config

input_file = "day01_input.txt"


def puzzles():
    current_freq = 0
    past_freq_set = set([])
    found_duplicate = False
    puzzle_loops = 0
    solution = [None, None]

    with open(input_file) as puzzle_in:
        while not found_duplicate:

            logging.debug("interation: {}, frequency: {}".format(
                puzzle_loops, current_freq))

            for line in puzzle_in:
                past_freq_set.add(current_freq)
                current_freq = eval("{} {}".format(current_freq, line))
                if current_freq in past_freq_set and not found_duplicate:
                    found_duplicate = True
                    solution[1] = current_freq

                    logging.debug("duplicate: {} ({} iterations)".format(
                        current_freq, puzzle_loops+1))
                    break

            if puzzle_loops == 0:
                solution[0] = current_freq

            puzzle_loops += 1
            puzzle_in.seek(0)
    return solution


if __name__ == "__main__":
    print("Advent of Code 2018, Day 1")
    #logging.basicConfig(level=logging.DEBUG)
    puzzle_1, puzzle_2 = puzzles()
    print("Puzzle 1: {}\nPuzzle 2: {}".format(puzzle_1, puzzle_2))
