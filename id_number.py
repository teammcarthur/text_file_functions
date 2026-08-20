'''
    Author: Chris M
    Version: 1.0
    Date: 20/08/26
    Description: Improved ID number program
'''


#-----Libraries-----
import random
import time
import string
import os

#-----Functions-----


#-----Main Routine-----
if(__name__ == "__main__"):
    while(True):
        first_name = input("Please enter your first name")
        if(len(first_name) < 2 or len(first_name) > 20 or not first_name.isalpha):
            print("Please enter a valid name")
            continue
        else:
            break