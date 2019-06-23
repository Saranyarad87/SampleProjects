# Programming test for Canary

## Bubble Sort program

This is an implementation of a bubble sort algorithm. The program prompts an input of the type eg. Numeric or Alphabet for sorting.Once you make a choice enter the list of number or character with spaces and hit ENTER. The program can sort asc or desc for the numbers.
The program will output the sorted string or number.

#### Example of inputs: 10 23 4 5  [ OR ] tree bad cat 

#### Sample outputs ( with asc sort for numbers): 4 5 10 23 [ OR ] bad cat tree

## Alphanumeric Sort

This program will sort an alphanumeric string in the order of numbers,lower case, upper case and other characters. The program will prompt for an input.

 ###### **Design choices for the Alpha numeric sort**
 For this implementation I use python 3 in-built sort and sorted implementation. There seems to some limiation with this function as a special character like '@' would cause the subsequent character/numbers to be treated as special characters as well. As such in those cases the sorting seems to be slightly off.

#### Example input : Az114d7$&
