import numpy as np
import pandas as pd
import re
from collections import OrderedDict

test_input = "Step C must be finished before step A can begin.\n\
                Step C must be finished before step F can begin.\n\
                Step A must be finished before step B can begin.\n\
                Step A must be finished before step D can begin.\n\
                Step B must be finished before step E can begin.\n\
                Step D must be finished before step E can begin.\n\
                Step F must be finished before step E can begin."

pattern = re.compile(".*Step (?P<prereq>\S) must be finished before step (?P<step>\S) can begin.*")

#data = test_input.split('\n')
#data = reddit_test.split('\n')

input_file = "day07_input.txt"
data = np.loadtxt(input_file, dtype=str, delimiter='\n')

# Generate a list of prerequisite steps
prereq = OrderedDict()
for each in data:
    inst = pattern.match(each).groupdict()
    if inst['step'] in prereq:
        prereq[inst['step']].append(inst['prereq'])
    else:
        prereq[inst['step']] = [inst['prereq']]

# Search and insert keys for letters that have no prereqs,
# these need to be at the front
alphabet = list(map(chr, range(65, 91)))
for letter in alphabet:
    if letter not in prereq:
        prereq.update({letter: []}) # insert missing letter
#       prereq.move_to_end(letter, last=False) # move to front

# Sort everything alphabetically
# Sort Keys
prereq = OrderedDict(sorted(prereq.items(), key=lambda t: t[0]))
# Sort Values
for key, value in prereq.items():
    value.sort()

# Sort the list into order. (Flags are a mess but it works)

def loop(prereq, order=[]):
    exhausted_list_flag = False
    while True:
        if len(prereq) == 0:  # Loop until prereq list is empty
            return order
        modified_prereqs = False
        for key, value in prereq.items():
            # Check prereqs, abort check if unsatisfied prereq found
            prereqs_met = True
            for p in value:
                if p not in order:
                    if exhausted_list_flag:
                        prereqs_met = all(map(lambda x: x in order, prereq[p]))
                        if prereqs_met:
                            #print("Adding {} from prereq list".format(p))
                            order.append(p)
                            prereq.pop(p)
                            exhausted_list_flag = False
                            prereqs_met = False
                            modified_prereqs = True
                            break
                    prereqs_met = False
                    break
            #  All prereqs are met, add key and remove from prereq list
            if prereqs_met:
                #print("Adding {} from key list".format(key))
                order.append(key)
                prereq.pop(key)
                modified_prereqs = True
                exhausted_list_flag = False
                prereqs_met = False
                break # Restart back at top of list
            # Reached end of list without adding anything
            if modified_prereqs:
                exhausted_list_flag = False
                prereqs_met = False
                break
        if not modified_prereqs:
            exhausted_list_flag = True

order = loop(prereq)
print("".join(order))