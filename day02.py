# Advent of Code 2018
# Day 2
# Brian Irelan

import logging

input = "day02_input.txt"

def puzzles():
    return [_puzzle_one(), _puzzle_two()]

def _puzzle_one():
    two_of_letter = 0
    three_of_letter = 0

    with open(input) as f:
        for line in f:
            checked_letters = []
            letter_count_list = []
            for letter in line.strip('\n'):
                if letter not in checked_letters:
                    letter_count_list.append(line.count(letter))
                    checked_letters.append(letter)
            two_of_letter += 1 if letter_count_list.count(2) else 0
            three_of_letter += 1 if letter_count_list.count(3) else 0
            logging.debug("Line: {} Twos: {} Threes: {}".format(
                line, letter_count_list.count(2), letter_count_list.count(3)))
    return two_of_letter * three_of_letter

def _puzzle_two():
    with open(input) as f:
        i = 0
        for line1 in f:
            i+=len(line1)+1
            for line2 in f:
                logging.debug("Comparing: '{}' and '{}'".format(
                    line1.strip(), line2.strip()))
                match_count = 0
                for index, letter in enumerate(line1.strip()):
                    if letter == line2.strip()[index]:
                        logging.debug("Matched: {} {}".format(
                            letter, line2[index]))
                        match_count += 1
                if match_count > 0:
                    logging.debug("Match Count: {} of {}".format(
                        match_count, len(line1.strip())))
                if match_count == len(line1.strip())-1: # Matched all chars but 1
                    logging.info("Found Prototype Fabric IDs: {}, {}".format(line1.strip(), line2.strip()))
                    return "".join(sorted(set(line1).intersection(line2),key=line1.index))
            f.seek(i)

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    print("Processing Input...", flush=True)
    puzzle_one, puzzle_two = puzzles()
    print("Puzzle 1): {}".format(puzzle_one))
    print("Puzzle 2): {}".format(puzzle_two))