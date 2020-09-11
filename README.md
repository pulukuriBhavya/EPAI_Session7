# session7
Session 7 is concentarted on **First Class Functions Part 1**
***
- This session is all about first class functions like Map, Filter, Zip, Reducing and Partial functions
## Getting Started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose.

### Prerequisites
***
Before string session check if all the required packages (pytest) are installed. Packages can be installed using the following code.
```
 pip install pytest
 ```

### Session7.py
***

Session7.py helps getting hands on concepts of Functional Parameters.

- isfib() function checks if the given number is a fibonacci number. Input parameters for isfib() are List of numbers
- add_even_odd() function will give the sum of an even and odd number. Input parameters for add_even_odd() are two lists of numbers
- remove_vowel() function will remove the vowels from the given string. Input parameters for remove_vowel() function is a string
- relu() function cimplements the functionality of ReLU. Input parameters for relu()() function is a List of numbers
- char_shift() function shifts each character of the given string by five places. Input parameters for char_shift() function is a string. 
- swear_words_check() function checks if there are any swear words in the given input. Input parameters for swear_words_check() function is a string.
- add_even() function adds all the even numbers in the list. Input parameters for add_even() function is a List of numbers.
- big_char() function looks for the biggest character in the string. Input parameters for big_char() function is a list of characters.
- list_sum() function returns the sum after adding every 3rd element in a list. Input parameters for list_sum() function is a List of numbers.
- num_plate() function  generates 15 random number plates.
- num_plate_partial() function generates 15 random number plates. Input parameters for num_plate_partial() function are state code of 2 characters, start and end range for number plate.


### test_session7.py

***

test_session7.py consists of 18 test cases which needs to be cleared.

- test_fourspace to check for indentation.
- test_function_name_had_cap_letter function name having capital letter.
- test_functions_avaiable to check if all the functions are implemeted.
- test_readme_exists to check if the README file exists
- test_readme_contents to check if the README content is exceding 400 words
- test_readme_file_for_formatting() to check for proper formatting
- test_isfib() to check if the function isfib() is returning fibonacci number
- test_add_even() to check if the function is giving sum of even and odd numbers in the given lists
- test_remove_vowel() to check if the function is returing characters after remmoving vowels
- test_relu() to check if the function is giving proper ReLU output for the given input
- test_sigmoid() to check if the function is giving proper Sigmoid output for girvn input
- test_char_shift() to check if the function is returning characters after shiting each by 5 characters
- test_swear_words_check() to check if the function is checking for swear words
- test_add_even() to check if the function is returning sum of all even nnumbers in the given input
- test_big_char() to check if the function is returning the biggest character of the given characters
- test_list_sum() to check if the function is returning the sum of every 3rd element
- test_num_plate() to check if the numper plate generated is in proper format
- test_num_plate_partial() to check if we are able to change the state code using partial functions