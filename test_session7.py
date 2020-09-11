import pytest
import inspect
#from test_utils import *
import re
import os.path
import sys

import session7

num_list = [0,1,5,7,12]


def test_fourspace():
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


FUNCTION_CHECK_FOR = [
    'isfib',
    'add_even_odd',
    'remove_vowel',
    'relu',
    'char_shift',
    'swear_words_check',
    'add_even',
    'big_char',
    'list_sum',
    'num_plate',
    'num_plate_partial'
]


def test_functions_avaiable():
    FUNCTIONSAVAILABLE = True
    f = open("session7.py", "r")
    content = f.read()
    f.close()
    for c in FUNCTION_CHECK_FOR:
        if c not in content:
            FUNCTIONSAVAILABLE = False
            pass
    assert FUNCTIONSAVAILABLE == True, "You have not implemented all the functions"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

README_CONTENT_CHECK_FOR = [
    'isfib',
    'add_even_odd',
    'remove_vowel',
    'relu',
    'char_shift',
    'swear_words_check',
    'add_even',
    'big_char',
    'list_sum',
    'num_plate',
    'num_plate_partial',
    'Zip',
    'Map',
    'Filter',
    'even',
    'odd'
]

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_isfib():
    r = session7.isfib(num_list)
    assert r == [0, 1, 5], "Your function is not working properly"

def test_add_even():
    r = session7.add_even_odd([1,2,3,4,5,6],[8,9,10,11,12,13])
    assert r == [11, 15, 19], "Your function is not working properly"


def test_remove_vowel():
    r = session7.remove_vowel('koundinya')
    assert r == ['k', 'n', 'd', 'n', 'y'], "Your function is not working properly"


def test_relu():
    r = session7.relu([1,5,-9,32,-45])
    assert r == [1, 5, 0, 32, 0], "Your function is not working properly"


def test_sigmoid():
    r = session7.sigmoid([43,45,65,78])
    assert r == [1.0, 1.0, 1.0, 1.0], "Your function is not working properly"

def test_char_shift():
    r = session7.char_shift('azxcv')
    assert r == ['f', 'e', 'c', 'h', 'a'], "Your function is not working properly"


def test_swear_words_check():
    r = session7.swear_words_check('''A visit to a goddamn historical place is jackoff always an gangbangs exciting experience. It is a fascinating adventure.
I had one such experience during the last summer vacations, when I visited Hyderabad.
With my family, I reached Hyderabad by train. After some rest, we undertook a visit to Hyderabad.
Hyderabad is a historical city.We visited the Char Minar first. Char Minar is located in Hyderabad in Andhra Pradesh, India.
It was built by Quli Qutub Shah in 1591. The Char Minar is an inseparable part of the history of Hyderabad.
Hyderabad is famous for its charming minarets Charminar.
The city of Hyderabad is often identified with the majestic Charminar.
Its enormous size and majestic splendor attracts a number of visitors.
Char Minar means 'Four minarets' and is built on a square platform with steps going to the top.
On the western side of the second storey was a mosque where the King would climb up to pray.
Around the Char Minar there were fountains.
The Char Minar is a splendid piece of architecture standing in the heart of the city of Hyderabad.
By noon, we had completed the tour of Char Minar and returned back. I enjoyed my trip to the Char Minar very much.
It was really an unforgettable experience which apart from being intellectually rewarding gave us a glimpse of our country's proud history.''')
    assert r == [False, False, False, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], "Your function is not working properly"


def test_add_even():
    r = session7.add_even([2,3,4,5,6,7,8,9])
    assert r == 20, "Your function is not working properly"


def test_big_char():
    r = session7.big_char(['a','h','y','b','z'])
    assert r == 'z', "Your function is not working properly"


def test_list_sum():
    r = session7.list_sum([1,2,3,4,5,6,7,8,9])
    assert r == 18, "Your function is not working properly"


def test_num_plate():
    r = session7.num_plate()
    assert re.match('[KA]+[0-9][0-9]+[A-Z][A-Z]+[0-9][0-9][0-9][0-9]',r[1]), "Your function is not working properly"


def test_num_plate_partial():
    r = session7.num_plate_generator('DL')
    assert re.match('[DL]+[0-9][0-9]+[A-Z][A-Z]+[0-9][0-9][0-9][0-9]',r[1]), "Your function is not working properly"






