############# ASSIGNMENT A
#%%  Coding Exercise 3:
# 1.	Write a string that returns just the letter ‘r’ from ‘Hello World’
#       For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. 
#       Don’t assign a variable name to the string.
print("Hello World"[8])

#%%
# 2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’
#       S=’hello’,what is the output of h[1]
print("thinker"[2:5])

#%%
# 3.	S=’Sammy’ what is the output of s[2:]” -- mmy
print('Sammy'[2:])


#%%
# 4.	‘Mississippi’ set function
print(set('Mississippi'))


#%%
# 5.	Palindrome
import string 

numberOfPhrases = int(input("How many phrases?"))
phraseList = []
i = 1
while i <= numberOfPhrases:
    phrase = input("Phrase {}/{}:".format(i, numberOfPhrases))
    phraseList.append(phrase)
    i += 1
else:
    pass


def isPalindrome(phrase):
    new_string = phrase.lower().replace(' ', '').translate(str.
                    maketrans('','', string.punctuation))
    if new_string == new_string[::-1]:
        return 'Y'
    else:
        return 'N'


# result = ['Y' for x in phraseList if isPalindrome(x) else 'N']
result = list(map(lambda x: isPalindrome(x), phraseList))

print(phraseList, result)



########## ASSIGNMENT B
# %% Coding Exercise 4:
# 1.	Create a list with one number, one word and one float value. Display the output of the list.
ones = [1, 'one', 1.0] 
print(ones)

#%% 2.	I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.  
#                               A: Refer to both list index and nested list index
nested_list = [1,1,[1,2]]
print(nested_list[2][1])

#%% 3.	lst=['a','b','c'] What is the result of lst[1:]?    A: ['b','c']
lst=['a','b','c']
print(lst[1:])

#%% 4.	Create a dictionary with weekdays an keys and week index numbers 
#       as values.do assign dictionary to a variable
weekdays = {
            'Sunday':1, 
            'Monday':2, 
            'Tuesday':3, 
            'Wednesday':4, 
            'Thursday':5, 
            'Friday':6, 
            'Saturday':7
            }

#%% 5.	d ={‘k1’:[1,2,3]} what is the output of d[k1][1]     A: 2
d = {'k1':[1,2,3]}
print(d['k1'][1])

#%% 6.	Can you create a list [1,[2,3]] into a tuple
tuple_list = (1, (2,3))
print(tuple_list)

#%% 7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.
word_set = set("Mississippi")
print(word_set)

# 8.	Can you add an element ‘X’ to the above created set
word_set.add('x')
print(word_set)

# 9.	Output of set([1,1,2,3])    A: unique values only
print(set([1,1,2,3]))

#%% Question 1
#   Write a program which will find all such numbers which are divisible by 7 
#   but are not a multiple of 5,between 2000 and 3200 (both included).
#   The numbers obtained should be printed in a comma-separated sequence on a single line.

def findNumbers():
    numbers = []
    x = 2000
    while x <= 3200:
        if x%7 == 0 and  x%5 != 0:
            numbers.append(x)
            x += 1
        else:
            x += 1
    return numbers

findNumbers() 


#%% Question 2
# Write a program which can compute the factorial of a given numbers.
	# The results should be printed in a comma-separated sequence on a single line.
	# Suppose the following input is supplied to the program:

# import math
number = int(input("Enter an integer:"))
# print(math.factorial(number))
                                        # Two Ways (import Math, Homemade)
def factorial(x):
    num = x
    while (x-1) > 0:
        num = num*(x-1)
        x -= 1
    return num

factorial(number)


#%% Question 3
# With a given integral number n, write a program to generate 
# a dictionary that contains (i, i*i) such that is an integral
# number between 1 and n (both included). and then the program 
# should print the dictionary.

number = int(input("Enter an integer:"))

def createDictionary(number):
    key = 1
    sq_dict = {}
    while key <= number:
        sq_dict[key] = key**2
        key += 1
    return sq_dict

print(createDictionary(number))


#%% Question 4
# Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.

number_list = input("Please enter a sequence of \
                        comma-separated numbers:").split(',')
asList = [int(x) for x in number_list]
asTuple = tuple(asList)
print("List:",asList)
print("Tuple:",asTuple)



# %% Question 5
# Define a class which has at least two methods:
# 	getString: to get a string from console input
# 	printString: to print the string in upper case.

class GetPrintString():
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input("Enter a string:")
    
    def printString(self):
        print(self.s.upper())

test = GetPrintString()
test.getString()
test.printString()
# %%

###### ASSIGNMENT C

#%% Three is a Crowd

# •	Make a list of names that includes at least four people.
# •	Write an if test that prints a message about the room being 
#   crowded, if there are more than three people in your list.
# •	Modify your list so that there are only two people in it. 
#   Use one of the methods for removing people from the list, 
#   don't just redefine the list.
# •	Run your if test again. There should be no output this time, 
#   because there are less than three people in the list.
# •	Bonus: Store your if test in a function called something 

names = ['jim','sidhartha','ganesh', 'jill']

class tooManyPeople:
    def __init__(self,list):
        self.list = list

    def crowdTest(self):
        if len(self.list) > 3:
            return print("the room is... crowded")

    def kickOut(self):
        return self.list.pop()

names = tooManyPeople(names)

print(names.list)
print(names.crowdTest())
print(names.kickOut())
print(names.kickOut())
print(names.list)
print(names.crowdTest())

# Part II
names2 = ['jim','sidhartha','ganesh', 'jill']

class sillyGame:
    def __init__(self,list):
        self.list = list

    def crowdTest(self):
        if len(self.list) > 3:
            return print("the room is... crowded")
        else:
            return print("the room is... not very crowded")

    def kickOut(self):
        return self.list.pop()

names2 = sillyGame(names2)

print(names2.list)
print(names2.crowdTest())
print(names2.kickOut())
print(names2.kickOut())
print(names2.list)
print(names2.crowdTest())

#%%  Six is a Mob

names2 = ['jim','sidhartha','ganesh', 'jill', 'xander', 'jacque', 'miguel','mariana', 'sweta', 'taryn','carl', 'ayelet']

class sixMob:
    def __init__(self,list):
        self.list = list

    def crowdTest(self):
        if len(self.list) > 5:
            return print("there is a mob in the room")
        elif len(self.list) > 2:
            return print("the room is crowded")
        elif len(self.list) > 0:
            return print("the room is not crowded")
        else:
            return print("the room is empty")

    def kickOut(self):
        return self.list.pop()

names2 = sixMob(names2)

print(names2.list)
print(names2.crowdTest())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.kickOut())
print(names2.list)
print(names2.crowdTest())
print(names2.kickOut())
print(names2.kickOut())
print(names2.list)
print(names2.crowdTest())
print(names2.kickOut())
print(names2.kickOut())
print(names2.list)
print(names2.crowdTest())
# %%
