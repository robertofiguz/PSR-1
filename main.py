#!/usr/bin/env python3
import argparse
from ast import Str
from random import Random, choice, random, sample
import string
from datetime import datetime
import getch
parser = argparse.ArgumentParser(description='Typing test')

parser.add_argument(
    '-utm',
    '--use_time_mode',
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


class Test:
    def __init__(self, utm: bool, max: int):
        self.type = utm
        self.max = max
        self.logs = []
        # self.logs = {'accuracy': 0.0,
        #              'inputs': [Input(requested='v', received='s', duration=0.11265206336975098),
        #                         Input(requested='w', received='d',
        #                               duration=0.07883906364440918),
        #                         Input(requested='d', received='a',
        #                               duration=0.0720210075378418),
        #                         Input(requested='a', received='s',
        #                               duration=0.0968179702758789),
        #                         Input(requested='b', received='d', duration=0.039067983627319336)],
        #              'number_of_hits': 0,
        #              'number_of_types': 0,
        #              'test_duration': 0,
        #              'test_end': '',
        #              'test_start': '',
        #              'type_average_duration': 0,
        #              'type_hit_average_duration': 0,
        #              'type_miss_average_duration': 0}

        print("Input any key to start the test")
        getch.getch()
        if utm:
            self.timeMode(max)
        else:
            self.countMode(max)

    def logResults(self):
        pass

    def getInput(self):
        letter = choice(string.ascii_lowercase)
        print(f'Input letter {letter}')
        userInput = getch.getch()
        if letter != userInput:
            print("wrong")
        else:
            print("correct")

        self.logs.append({"requested": letter, "input": userInput})

    def countMode(self, max):
        print(f"Starting test in count mode - {max} sequences")
        for i in range(max):
            self.getInput()

    def timeMode(self, max):
        print(f"Starting test in time mode with duration {max}")
        startTime = datetime.now()
        while not (datetime.now()-startTime).total_seconds() >= max:
            self.getInput()
        if (datetime.now()-startTime).total_seconds() > max:
            print(f"Time exceed by {(datetime.now()-startTime).total_seconds()-max}")


if __name__ == '__main__':

    args = parser.parse_args()
    test = Test(args.use_time_mode, args.max_value)
    test.logResults()
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
