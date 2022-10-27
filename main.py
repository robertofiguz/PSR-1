#!/usr/bin/env python3
import argparse
from random import choice
import string
from datetime import datetime
import getch
from termcolor import colored
from time import time
import pprint
from collections import namedtuple

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

        self.Input = namedtuple('Input',
                                ['requested', 'received', 'duration'])

        self.type = utm
        self.max = max
        self.logs = {'accuracy': 0.0,
                     'inputs': [],
                     'number_of_hits': 0,
                     'number_of_types': 0,
                     'test_duration': "",
                     'test_end': "",
                     'test_start': datetime.today(),
                     'type_average_duration': 0,
                     'type_hit_average_duration': 0,
                     'type_miss_average_duration': 0}

        print("Input any key to start the test")
        getch.getch()
        if utm:
            self.timeMode(max)
        else:
            self.countMode(max)

    def logResults(self):
        self.logs['test_end'] = datetime.today()
        self.logs['test_duration'] = (
            self.logs['test_end']-self.logs['test_start']).total_seconds()
        self.logs['types'] = len(self.logs['inputs'])
        self.logs['number_of_types'] = len(self.logs['inputs'])
        self.logs['accuracy'] = self.logs['number_of_hits'] / \
            self.logs['number_of_types']
        self.logs['test_end'] = self.logs['test_end'].strftime('%c')
        self.logs['test_start'] = self.logs['test_start'].strftime('%c')
        self.logs['type_average_duration'] = self.logs['test_duration'] / \
            self.logs['number_of_types']
        try:
            self.logs['type_hit_average_duration'] = self.logs['type_hit_average_duration'] / \
                self.logs['number_of_hits']
        except ZeroDivisionError:
            pass
        try:
            self.logs['type_miss_average_duration'] = self.logs['type_miss_average_duration'] / \
                (self.logs['types']-self.logs['number_of_hits'])
        except ZeroDivisionError:
            pass
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.logs)
        exit()

    def getInput(self):
        letter = choice(string.ascii_lowercase)
        print(f'Input letter {letter}')
        startTime = time()
        userInput = getch.getch()
        endTime = time()
        elapsed = endTime-startTime
        if userInput == " ":
            self.logResults()
        if letter != userInput:
            self.logs['type_miss_average_duration'] += elapsed
            print("wrong input: ", colored(userInput, 'red'))
        else:
            self.logs['number_of_hits'] += 1
            self.logs['type_hit_average_duration'] += elapsed
            print("correct input: ", colored(userInput, 'green'))

        self.logs['inputs'].append(self.Input(letter, userInput, elapsed))

    def countMode(self, max):
        print(f"Starting test in count mode - {max} sequences")
        for i in range(max):
            self.getInput()

    def timeMode(self, max):
        print(f"Starting test in time mode with duration {max}")
        startTime = time()
        while not (time()-startTime) >= max:
            self.getInput()
        if (time()-startTime) > max:
            print(f"Time exceed by {(time()-startTime)-max}")


if __name__ == '__main__':

    args = parser.parse_args()
    test = Test(args.use_time_mode, args.max_value)
    test.logResults()
