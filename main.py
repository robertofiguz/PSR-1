#!/usr/bin/env python3
import argparse
from ast import Str
from random import Random, choice, random, sample
import string
from datetime import datetime
parser = argparse.ArgumentParser(description='Typing test')

parser.add_argument(
    '-utm',
    '--use_time_mode' ,
    action=argparse.BooleanOptionalAction,
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

def results():
    pass

def time_mode(max):

    startTime = datetime.now()

    while not (datetime.now()-startTime).total_seconds() >= max:
        letter = choice(string.ascii_lowercase)
        userInput = input(f'Input letter {letter} \n')
        if userInput != letter:
            print("wrong")
        else:
            print("correct")

def count_mode(max):
    for i in range(max): 
        letter = choice(string.ascii_lowercase)
        userInput = input(f'Input letter {letter} \n')
        if userInput != letter:
            print("wrong")
        else:
            print("correct")


if __name__ == '__main__':
    args = parser.parse_args()
    max = args.max_value
    mode = args.use_time_mode
    print(max)
    if mode:
        time_mode(max)
    else:
        count_mode(max)

    results()


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
