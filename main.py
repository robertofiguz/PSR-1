#!/usr/bin/env python3
import argparse
from ast import Str
from random import Random, choice, random

parser = argparse.ArgumentParser(description='Typing test')

parser.add_argument(
    '-utm',
    '--use_time_mode' ,
    help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.'
    )
# bool is accepting any string as it only converts input into bool and therefore it will take any string as true, even false
parser.add_argument(
    '-mv',
    '--max_value',
    type=int,
    help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.'
    )

args = parser.parse_args()

def main():
    pass

if __name__ == '__main__':
    args = parser.parse_args()
    max = args.max_value
    mode = args.use_time_mode
    print(mode)

'''
TODO:
- read input from user
- wait for input from user to start the test
- how to randomize letter? 
    - create a list with all the letters and use choice?
    - is there a more elegant way to implement this?
- compare the entry with the letter shown
- define space as exit from the loop
- logs:
    - requested letter
    - received letter
    - time from being shown until the input
    (use a namedtuple for this)

    - after the test is finnished, calculate:
        - test_duration
        - test_start
        - test_end
        - number_of_hits
        - accuracy
        - type_average_duration
        - type_hit_average_duration
        - type_miss_average_duration

    print the resulting dict. using prettyprint
'''
