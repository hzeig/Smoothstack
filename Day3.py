#%% 1.	 Write a Python program to find those numbers which 
#       are divisible by 7 and multiple of 5, between 1500 
#       and 2700 (both included). Go to the editor

result = []
for x in range(1500, 2700):
    if x%7 == 0 and x%5 == 0:
        result.append(x)
print(result)


#%% 2.	 Write a Python program to convert temperatures to 
#        and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 
# [ where c = temperature in celsius and 
#                           f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 

temp = int(input("Enter degrees: (i.e. 32,67)"))
which = input("Enter 'F' for Farenheit or 'C' for Celsius:")
def tempConverter(which, temp):
    which = which.upper().strip()
    if which != 'C' and which != 'F':
        return print("Error: incorrect input")
    if which == 'C':
        F = temp*(9/5) + 32
        return print("{}°C is {}° in Farenheit".format(temp,F))
    else:
        C = (temp-32)*(5/9)
        return print("{}°F is {}° in Celsius".format(temp,C))

tempConverter(which, temp)

#%% 3.	 Write a Python program to guess a number 
#       between 1 to 9. Go to the editor
#       Note : User is prompted to enter a guess. 
#       If the user guesses wrong then the prompt 
#       appears again until the guess is correct, 
#       on successful guess, user will get a "Well 
#       guessed!" message, and the program will exit.

import random

number = random.randrange(1,9,1)
guess = int(input("Guess any number between 1 and 9:"))

def guessingGame(number,guess):
    while guess and number:
        if guess > 9:
            print("Error: guess out of range")
            guess = int(input("Guess again!"))
            continue
        elif guess == number:
            return print("Well guessed!")
        else:
            guess = int(input("Guess again!"))
            continue

guessingGame(number,guess)


#%% 4.	Write a Python program to construct the 
#       following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

symbol = input("Enter symbol:")
length = int(input("Enter number of rows, e.g. 7:"))

for row in range(length + 1):
    for column in range(row):
        print(symbol, end='')
    print()

for row in range(length, 0, -1):
    for column in range(row-1):
        print(symbol, end='')
    print()


#%% 5.	 Write a Python program that accepts a word 
#       from the user and reverse it. Go to the editor

word = input("Type a word:")
print(word[::-1])

#%% 6.	 Write a Python program to count the number 
#       of even and odd numbers from a series of numbers. 
#       Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output : 
# Number of even numbers : 5
# Number of odd numbers : 4

series = input("Enter a series of numbers, \
            e.g. '1, 2, 3, 4, 5, 6, 7, 8, 9'").split(',')
series = [int(x) for x in series]
even = [x for x in series if x%2 == 0]
odd = [x for x in series if x%2 != 0]
print("Number of even numbers: {}".format(len(even)))
print("Number of odd numbers: {}".format(len(odd)))

#%% 7.	Write a Python program that prints each item and 
#       its corresponding type from the following list.

import string

datalist = [1452, 11.23, 1+2j, True, 'w3resource', \
            (0, -1), [5, 12], {"class":'V', "section":'A'}]

def dtypes(list):
    dict = {}
    for item in list:
        strItem = str(item)
        dict[strItem] = str(type(item))[7:].replace('\'','').replace('>', '')
    return dict


print(dtypes(datalist))

import pandas as pd
print(pd.DataFrame(dtypes(datalist)))

#%% 8.	Write a Python program that prints all the numbers 
#       from 0 to 6 except 3 and 6.
#       Note : Use 'continue' statement. 
#       Expected Output : 0 1 2 4 5 

print([x for x in range(0,6) if x != 3 and x != 6])

# %%
