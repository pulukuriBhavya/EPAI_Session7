import math
from functools import reduce
from functools import partial
import random

fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
vowels = ['a', 'e', 'i', 'o', 'u']


def isfib(num_list):
    '''This function will check if the given number is a fibonacci number

        Input: List of numbers

        Output:List of fibonacci numbers
    '''
    return list(filter(lambda x: 1 if x in fib_list else 0, num_list))


def add_even_odd(list1, list2):
    '''This function will give the sum of an even and odd number

        Input: two lists of numbers

        Output:sum
    '''
    return [x+y for x, y in zip(list1, list2) if (x % 2 == 0 and y % 2 != 0)]


def remove_vowel(text):
    '''This function will remove the vowels from the given string

        Input: string

        Output:list of chars after removing vowels from given string
    '''
    return [x for x in text if x not in vowels]


def relu(array):
    '''This function implements the functionality of ReLU

        Input: List of numbers

        Output:ReLU output of given numbers
    '''
    return [x if x >= 0 else 0 for x in array]


def sigmoid(input_list):
    '''This function implements the functionality of Sigmoid

        Input: List of numbers

        Output:Sigmoid output of given numbers
    '''
    return [1/(1 + math.exp(-x)) for x in input_list]


def char_shift(input_string):
    '''This function shifts each character of the given string by five places

        Input: string

        Output:list of characters after shifting each character of string by five places
    '''
    return [chr(ord(x)-21) if ord(x)+5 > ord('z') else chr(ord(x)+5) for x in input_string]


def swear_words_check(input_paragraph):
    '''This function checks if there are any swear words in the given input

        Input: string

        Output:True if it is a swear word else false
    '''
    with open('list.txt') as f:
        swear_word_list = [line.rstrip() for line in f]
    return [False if x not in swear_word_list else True for x in input_paragraph.split()]


def add_even(input_list):
    '''This function adds all the even numbers in the list

        Input: List of numbers

        Output: sum of even numbers in the list
    '''
    return reduce(lambda x, y: x + y if (x % 2 == 0 and y % 2 == 0) else x, input_list)


def big_char(char_list):
    '''This function looks for the biggest character in the string

        Input: list of characters

        Output:Biggest character in the list
    '''
    return reduce(lambda x, y: x if ord(x) > ord(y) else y, char_list)


def list_sum(input_list):
    '''This function returns the sum after adding every 3rd element in a list

        Input: List of numbers

        Output: sum of every 3rd element in the list
    '''
    return reduce(lambda x, y: x + y, input_list[2::3])


def num_plate():
    '''This function generates 15 random number plates

        Output: Number plates
    '''
    return ['KA' + str(random.randint(10, 100)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(random.randint(1000, 10000)) for i in range(15)]


def num_plate_partial(state_code, input1, input2):
    '''This function generates 15 random number plates

        Input: state code of 2 characters, start and end range for number plate

        Output:ReLU output of given numbers
    '''
    return [state_code + str(random.randint(10, 100)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(random.randint(input1, input2)) for i in range(15)]


num_plate_generator = partial(num_plate_partial, input1=1000, input2=10000)
