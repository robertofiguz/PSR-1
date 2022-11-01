#######################################################################################
#  Trabalho Prático 1 - PSR Typing Test 
# 
#  Elaborado por:
#       João Figueiredo 116189
#       Magda Leitão 98214
#       Roberto Figueiredo 116147
#######################################################################################

#!/usr/bin/env python3

import argparse # Argumentos de linha de comando
import string # usada para listar as letras do alfabeto
import getch # usada para ler o input do utilizador
import pprint # usada para imprimir o dicionário de resultados
from random import choice # usada para escolher uma letra aleatória
from datetime import datetime # usada para calcular o tempo de execução
from termcolor import colored # usada para imprimir o texto colorido, dependendo do resultado
from time import time # usada para calcular o tempo de execução
from collections import namedtuple # usada para criar um tipo de dados para guardar o input do utilizador


parser = argparse.ArgumentParser(description='Typing test') 

# Argumentos de linha de comando
# -utm, se definida, usa o valor de -mv como tempo limit em segundos
parser.add_argument(
    '-utm',
    '--use_time_mode',
    action=argparse.BooleanOptionalAction,
    help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.'
)
# -mv é o valor de tempo limite ou número de inputs limite
parser.add_argument(
    '-mv',
    '--max_value',
    type=int,
    required=True,
    help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.'
)

args = parser.parse_args()

#Definição de class Test 
class Test:
    def __init__(self, utm: bool, max: int):

        # namedtuple para guardar o input do utilizador
        self.Input = namedtuple('Input',
                                ['requested', 'received', 'duration'])

        self.type = utm
        self.max = max
        # dicionário para guardar os resultados
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

        # espera que o utilizador pressione qualquer tecla para iniciar o teste
        s = getch.getch()
        if s == " ":  # caso o utilizador pressa a tecla espaço, termina o teste
            self.logResults()
        if utm:
            self.timeMode(max)
        else:
            self.countMode(max)

    def logResults(self):
        #atuailiza o dicionário de resultados
        self.logs['test_end'] = datetime.today()
        self.logs['test_duration'] = (
            self.logs['test_end']-self.logs['test_start']).total_seconds()
        self.logs['types'] = len(self.logs['inputs'])
        self.logs['number_of_types'] = len(self.logs['inputs'])
        self.logs['test_end'] = self.logs['test_end'].strftime('%c')
        self.logs['test_start'] = self.logs['test_start'].strftime('%c')
            
        # caso o numero de types, hits or misses seja 0, definir como 0 para evitar divisão por 0
        if self.logs['number_of_types'] == 0:
            self.logs['accuracy'] = 0.0
            self.logs['type_average_duration'] = 0.0
        else:
            self.logs['type_average_duration'] = self.logs['test_duration'] / \
                self.logs['number_of_types']
            self.logs['accuracy'] = self.logs['number_of_hits'] / self.logs['number_of_types']
        if self.logs['number_of_hits'] == 0:
             self.logs['type_hit_average_duration'] = 0.0
             self.logs['type_miss_average_duration'] = 0.0
        else:
            self.logs['type_hit_average_duration'] = self.logs['type_hit_average_duration'] / self.logs['number_of_hits']
        if self.logs['number_of_types'] - self.logs['number_of_hits'] == 0:
            self.logs['type_miss_average_duration'] = 0.0
        else:
            self.logs['type_miss_average_duration'] = self.logs['type_miss_average_duration'] / (self.logs['types']-self.logs['number_of_hits'])
        
        #imprime o dicionário de resultados
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.logs)

        # guardar os resultados num ficheiro json
        with open(f'logs_{(self.logs["test_start"]).replace(" ", "_")}.json', 'w') as f:
            f.write(str(self.logs))
        exit()

    # função usada para lidar com o input do utilizador, incluindo a seleção da letra aleatória
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

    # função usada para o modo de quantidade de inputs
    def countMode(self, max):
        print(f"Starting test in count mode - {max} sequences")
        for i in range(max):
            self.getInput()

    # função usada para o modo de tempo
    def timeMode(self, max):
        print(f"Starting test in time mode with duration {max}")
        startTime = time()
        while not (time()-startTime) >= max:
            self.getInput()
        if (time()-startTime) > max:
            print(f"Time exceed by {(time()-startTime)-max}")


if __name__ == '__main__':

    args = parser.parse_args()
    #instanciar a class Test com os argumentos passados pelo utilizador
    test = Test(args.use_time_mode, args.max_value)
    #após terminar o teste, fazer log dos resultados
    test.logResults()

