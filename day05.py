
# coding: utf-8

# # Advent of Code 2018
# ### Day 5
# ### Brian Irelan

# In[1]:


import logging
logging.basicConfig(level=logging.INFO)

alphabet =  list(map(chr, range(97, 123)))


# In[2]:


def puzzles(data_in, remove_letter=''):
    # Preprocess data by removing one letter
    letters_removed = 0
    while(data_in.count(remove_letter)>0): # This is bad but I can't figure out why .pop and del are skipping letters
        for position, letter in enumerate(data_in):
            if letter.upper() == remove_letter.upper():
                del data_in[position]
                letters_removed += 1
                       
    found_reaction = True
    iteration_count = 0
    while(found_reaction):
        previous_letter = ''
        found_reaction = False
        for position, letter in enumerate(data_in):
            # If prevous letter is the letter but a different case
            if letter.upper() == previous_letter.upper() and letter != previous_letter:
                data_in.pop(position-1)
                data_in.pop(position-1)
                found_reaction = True
                previous_letter = ''
            else:
                previous_letter = letter
                
        iteration_count += 1

    data_in = "".join(data_in)
    
    logging.debug("Remaining Units ({} removed): {}, Iteration Count: {}, Letters Removed: {}".format(
        remove_letter if not '' else "None", len(data_in), iteration_count, letters_removed))
    return len(data_in)


# In[3]:


#raw_input = "dabAcCaCBAcCcaDA"
#data = list(raw_input)

input_file = "day05_input.txt"
f = open(input_file)
data = list(f.readlines()[0].strip())


# In[4]:


logging.info("Processing Part One...")
remaining = puzzles(data.copy())
logging.info("[Part One] Remaining Units: {}".format(remaining))


# In[5]:


logging.info("Processing Part Two...")
remaining = []
for letter in alphabet:
    logging.debug("Removing {}".format(letter))
    remaining.append(puzzles(data.copy(), letter))
    print(".",end='')

optimal_length = min(remaining)
optimal_letter = chr(remaining.index(optimal_length)+97)

logging.info("[Part Two] Remaining Units ({} removed): {}".format(optimal_letter.lower(), optimal_length))

