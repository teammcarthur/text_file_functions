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
#Function to remove all letters excluding the first letter from last name and concatenate the names and year
def string_slice(last_name, first_name, year):
    last_name = last_name[:1]
    year = str(year)[:3]
    combined_name = (first_name + last_name + str(year))
    return combined_name

def unique_code():
    code = random.randint(111, 999)
    return code
#-----Main Routine-----
if(__name__ == "__main__"):
    combined_name = ""
    code = 0
    while(True):
        first_name = input("Please enter your first name")
        if(len(first_name) < 2 or len(first_name) > 20 or not first_name.isalpha):
            print("Please enter a valid name")
            continue
        else:
            break
    while(True): #This loop validates the users input for last name
        last_name = input("Please enter your last name")
        if(len(last_name) < 2 or len(last_name) > 20 or not last_name.isalpha):
            print("Please enter a valid name")
            continue
        else:
            break
    year = random.randint(2025, 2050) #Stores a random number from 2025 to 2050
    string_slice(last_name, first_name, year)
    unique_code()
    username = combined_name + str(code)
    print(username)