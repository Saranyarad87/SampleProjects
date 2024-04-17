# Programming test samples

## Bubble Sort program

This is an implementation of a bubble sort algorithm. 
The program can sort in ascending or descending order if numbers are given as input and alphabetically if alphabets.
The program will output the sorted string or number.

#### Example of inputs: 10 23 4 5  [ OR ] tree bad cat 

#### Sample outputs ( with asc sort for numbers): 4 5 10 23 [ OR ] bad cat tree

in-built unit test cases covers the following:

TC1 - Testing with numbers with invalid sorting order
TC2 - Testing with numbers to sort in ascending order
TC3 - Testing with numbers to sort in descending order
TC4 - Testing with double and triple digit numbers to sort in ascending order
TC5 - Testing with alphabets with invalid answer to y/n question
Please re-run the program with valid input.
TC6 - Testing with alphabets sorted alphabetically
TC7 - Testing with alphabets sorted non-alphabetically
TC8 - Testing with words sorted alphabetically
TC9 - Testing with Invalid format selection instead of 1 for nmber and 2 for alphabets


## Alphanumeric Sort

This program will sort an alphanumeric string in the order of numbers,lower case, upper case and other characters. The program will prompt for an input.

 ###### **Design choices for the Alpha numeric sort**
 For this implementation I use python 3 in-built sort and sorted implementation. There seems to some limitation with this function as a special character like '@' would cause the subsequent character/numbers 
 to be treated as special characters as well. As such in those cases the sorting seems to be slightly off.

#### Example input : Az114d7$&
#### sample output: 7114dzA&$

in-built unit test cases covers the following:
TC1 - Testing chk_digit module
TC2 - Testing mysplit module
TC3 - Testing splitString_sort module
TC4 - Testing Alphanumeric sort with 3 different strings - 'A11a4' ,'D5(2sI45','H78g2!'
