# we need to be able to generate random number plate so a varaible for a randomized selection
import random 
# we can also do this for the date to allow the program to be able to calculate the date without any complex equation or process. it almost liek having a calener in teh program which can easily  know the age depending on the date you type
from datetime import datetime 

# the plate has three parts (ab 00 xyz) the first part (ab) shouldnt have letter (I, Q or Z) 
# while the last part (cde) shouldn't have the letter (I or Q) so what we can do is define it at the start 


FIRST = "ABCDEFGHJKLMNOPRSTUVWXY"
LAST = "ABCDEFGHJKLMOPRSTUVWXYZ"
# using this we can already cancel out the unwant letters in each section which are I, Q or Z

# now lets start building the main part 

# using a define function("def") we can assigned certain words to a function so we ont haev to type out long lines of code instead we can just type the word we already defined 

def function():
    # a good example is the tidy function we are going to use

def tidy (plate):
    # when a user types a plate number this convert all to lower case letters to upper case as well as removing all unneccesary space
    plate = plate.upper().replace(" ","")
    return plate

