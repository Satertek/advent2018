# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:46:03 2018

@author: IrelanBT

Advent of Code 2018
Day 2
            _
........... | Second Term
........... _
...#####...    ^
...#####...    | Fourth Term
...#####...    V
...#####...    _
...........
...........
...........
|-|
First Term

   |<->|
      Third Term

"""




import re
import numpy as np
import logging
from PIL import Image, ImageDraw


def puzzles(input_data):
    return _puzzle_one(input_data)

def _puzzle_one(input_data):

    f = open(input_data)
    raw_data = f.readlines()

    input_regex = '#(?P<id>\d+)\s@\s(?P<left_offset>\d+),(?P<top_offset>\d+):\s(?P<width>\d+)x(?P<height>\d+)'
    data = []
    for each in raw_data:
        data.append(re.search(input_regex, each).groupdict())

    data_length = len(data)
    combined_claim_map = np.array([[0],[0]])
    potential_claims = set([])

    for claim in data:
        logging.info("{:4d}/{:4d}".format(int(claim['id']),data_length))
        left_offset = int(claim['left_offset'])
        top_offset = int(claim['top_offset'])
        width = int(claim['width'])
        height = int(claim['height'])
        claim_id = int(claim['id'])


        height_of_map = left_offset + width
        width_of_map = top_offset + height
        combined_height = combined_claim_map.shape[1]
        combined_width = combined_claim_map.shape[0]

        if height_of_map < combined_height:
            height_of_map = combined_height
        if width_of_map < combined_width:
            width_of_map = combined_width

        this_claim_map = np.zeros([width_of_map,height_of_map])

        # Copy existing map
        for i in range(width_of_map):
            for j in range(height_of_map):
                try:
                    this_claim_map[i,j] = combined_claim_map[i,j]
                except IndexError:
                    pass

        # Draw new rectangle
        overlap_flag = False
        for i in range(width):
            for j in range(height):
                my_square_inch = this_claim_map[j + top_offset, i + left_offset]
                if my_square_inch != 0:
                    this_claim_map[j + top_offset, i + left_offset] = -1
                    overlap_flag = True
                    try:
                        potential_claims.remove(my_square_inch)
                    except KeyError:
                        pass  # Ignore if key isn't there
                else:
                    this_claim_map[j + top_offset, i + left_offset] = claim_id

        if not overlap_flag:
            potential_claims.add(claim_id)

        combined_claim_map = this_claim_map

    golden_claim = potential_claims
    overlap = np.count_nonzero(combined_claim_map == -1)
    return overlap, combined_claim_map, golden_claim


if __name__ == "__main__":
    #input_data = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
    #raw_data = input_data.split('\n')
    input_data = "day03_input.txt"
    logging.basicConfig(level=logging.INFO)
    logging.info("Processing Input...")
    overlap, combined_claim_map, golden_claims = puzzles(input_data)
    logging.info("Disputed Claims: {} sq. in.".format(overlap))
    logging.info("Unobstructed Claim #: {}".format(golden_claims))
    im = Image.fromarray(combined_claim_map)
    im.show()
    im.save("output.tiff")

