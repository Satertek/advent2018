# Advent of Code 2018
# Day 1
# Brian Irelan

# Config

input_file = "day01_input.txt"
enable_duplicate_search = True

# don't edit below

current_freq = 0
past_freq_set = set([])
found_duplicate = not enable_duplicate_search
puzzle_loops = 0

with open(input_file) as puzzle_in:
    while(not found_duplicate):
        for line in puzzle_in:
            past_freq_set.add(current_freq)
            current_freq = eval("{} {}".format(current_freq, line))
            if current_freq in past_freq_set and not found_duplicate:
                print("Found Duplicate Frequency: {}".format(current_freq))
                found_duplicate = True
        print("Frequency Calibration Offset {}: {}".format(puzzle_loops, current_freq))
        puzzle_loops += 1
        puzzle_in.seek(0)
