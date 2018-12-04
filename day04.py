# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:20:40 2018

@author: IrelanBT

Advent of Code 2018
Day 4


"""
import re

'''
test_input = ("[1518-11-01 00:00] Guard #10 begins shift\n"
              + "[1518-11-01 00:05] falls asleep\n"
              + "[1518-11-01 00:25] wakes up\n"
              + "[1518-11-01 00:30] falls asleep\n"
              + "[1518-11-01 00:55] wakes up\n"
              + "[1518-11-01 23:58] Guard #99 begins shift\n"
              + "[1518-11-02 00:40] falls asleep\n"
              + "[1518-11-02 00:50] wakes up\n"
              + "[1518-11-03 00:05] Guard #10 begins shift\n"
              + "[1518-11-03 00:24] falls asleep\n"
              + "[1518-11-03 00:29] wakes up\n"
              + "[1518-11-04 00:02] Guard #99 begins shift\n"
              + "[1518-11-04 00:36] falls asleep\n"
              + "[1518-11-04 00:46] wakes up\n"
              + "[1518-11-05 00:03] Guard #99 begins shift\n"
              + "[1518-11-05 00:45] falls asleep\n"
              + "[1518-11-05 00:55] wakes up")
'''

#raw_data = test_input.split('\n')

input_file = "day04_input.txt"
f = open(input_file)
raw_data = f.readlines()

input_regex = ('\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)\s(?P<hour>\d+):(?P<minute>\d+)\]'
             + '\s(Guard|(?P<action>\S+))\s(#?)(?P<id>\d+)?')
data = []
for each in raw_data:
    data.append(re.search(input_regex, each).groupdict())

sorted_data = sorted(data, key=lambda x: (x['month'],x['day'],x['hour'],x['minute']))

guard_id = {'guards':{}}
for record in sorted_data:
    if record['id']:
        current_guard = record['id']

    # Create key for guard if it doesn't exist
    try:
        guard_id['guards'][current_guard]
    except KeyError:
        guard_id['guards'].update({record['id']:
            {'minutes_asleep': ([0]*60)}})

    if record['action'] == "falls":  # asleep
        # Record time fell asleep
        fell_asleep = int(record['minute'])

    if record['action'] == "wakes":
        # Write time fell asleep and woke up to guard list
        for i in range(fell_asleep, int(record['minute'])):
            guard_id['guards'][current_guard]['minutes_asleep'][i] += 1

print("Guard\tSleep\tSleepiest\t\t\tSchedule")
print("ID#\tTime\tTime")
print("\tmin\tmin (#)\t000000000011111111112222222222333333333344444444445555555555")
print("\t\t\t012345678901234567890123456789012345678901234567890123456789")

sleepiest_times = []
for guard in list(guard_id['guards']):
    sleep_list = guard_id['guards'][guard]['minutes_asleep']
    this_sleepy_time = int(sleep_list.index(max(sleep_list)))
    heaviest_sleeper = sum(sleep_list)
    sleepiest_times.append({'guard':guard,
                            'total':heaviest_sleeper,
                            'min':this_sleepy_time,
                            'times':sleep_list[this_sleepy_time]})
    print("{:4d}\t{:3d}\t{:2d} ({:2d})\t{}".format(int(guard),
                              heaviest_sleeper,
                              this_sleepy_time,
                              sleep_list[this_sleepy_time],
                              "".join(("#" if x>9 else str(x)) for x in sleep_list) # keeps everything square
                              ))

sleepiest_guard = sorted(sleepiest_times,key=lambda x: x['total']).pop()
sleepy_guard_id = int(sleepiest_guard['guard'])
sleepy_guard_total = int(sleepiest_guard['total'])
sleepy_guard_min = int(sleepiest_guard['min'])
sleepy_guard_answer = sleepy_guard_id * sleepy_guard_min

consistant_guard = sorted(sleepiest_times,key=lambda x: x['times']).pop()
consistant_guard_id = int(consistant_guard['guard'])
consistant_guard_times = int(consistant_guard['times'])
consistant_guard_min = int(consistant_guard['min'])
consistant_guard_answer = consistant_guard_id * consistant_guard_min

print("\nSleepiest Guard (Strategy 1)\n#{:4d}\tfor {:2d} mins\tAnswer 1: {}\t".format(sleepy_guard_id,
                                                      sleepy_guard_min,
                                                      sleepy_guard_answer))
print("\nConsistant Sleep Schedule Guard (Strategy 2)\n#{:4d}\tat 00:{:2d}\tAnswer 2: {}".format(consistant_guard_id,
                                                      consistant_guard_min,
                                                      consistant_guard_answer))



