# ASSIGNMENT A

#%% 1.Create a function func() which prints a text ‘Hello World’

def helloWorld():
    return print("Hello World")

helloWorld()


#%% 2.Create a function which func1(name)  which takes a value 
#       name and prints the output “Hi My name is Google’

def greeting(name):
    return print("Hi, my name is {}.".format(name))

greeting("shmrow")


#%% 3.Define a function func3(x,y,z) that takes three arguments 
#       x,y,z where z is true it will return x and when z is 
#       false it should return y . func3(‘hello’goodbye’,false)

def trueOrFalse(x,y,z):
    return x if z else y

trueOrFalse('hello','goodbye',True)

#%% 4.define a function func4(x,y) which returns the product 
#     of both the values.
def func4(x,y):
    return x*y

func4(3,5)


#%% 5.define a function called as is_even that takes one argument, 
#     which returns true when even values is passed and false 
#       if it is not.

def is_even(number):
    return True if number%2 == 0 else False

is_even(9)


#%% 6.define a function that takes two arguments ,and returns 
#     true if the first value is greater than the second value 
#   and returns false if it is less than or equal to the second.

def func6(x,y):
    return True if x > y else False

func6(9,2)

#%% 7.Define a function which takes arbitrary number of 
#     arguments and returns the sum of the arguments.

def func7(*arg):
    return sum(arg)

func7(3,4,5,1,2)


#%% 8.Define a function which takes arbitrary number of 
#     arguments and returns a list containing only the 
#     arguments that are even.

def func8(*arg):
    return [x for x in arg if x%2 == 0]

func8(3,4,5,1,2)


#%% 9.Define a function that takes a string and returns 
# a matching string where every even letter is uppercase 
# and every odd letter is lowercase 

def func9(string):
    new_string = ""
    for i in range(len(string)):
        if i%2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string

func9("hello how are you?")


#%% 10.Write a function which gives lesser than a given 
#     number if both the numbers are even, but returns 
#     greater if one or both or odd.

def func10(x,y):
    if x%2 != 0 or y%2 != 0:
        return x if x > y else y
    else:
        return x if x < y else y

func10(4, 6)

#%% 11.Write a function which takes two-strings and returns 
#     true if both the strings start with the same letter.

def func11(s1, s2):
    return True if s1[0] == s2[0] else False

func11('silly','sass')

#%% 12.Given a value,return a value which is twice as 
#     far as other side of 7

def func12(number):
    # take absolute value of difference between entered value and 7
    diff = abs(number - 7) 
    if number > 7:
        return 7 - diff*2 
    else:
        return 7 + diff*2

func12(5)


#%% 13.A function that capitalizes first and fourth 
#       character of a word in a string.

def func13(string):
    new_string = ""
    for i in range(len(string)):
        if i == 0 or i == 3:
            new_string += string[i].upper()
        else:
            new_string += string[i]
    return new_string

func13("blahblahblah"


# ASSIGNMENT B

# %%
# Imagine an accounting routine used in a book shop. It works on a list 
# with sublists, which look like this: 

# Order Number	Book Title and Author	Quantity	Price per Item
# 34587	Learning Python, Mark Lutz	4	40.95
# 98762	Programming Python, Mark Lutz	5	56.80
# 77226	Head First Python, Paul Barry	3	32.95
# 88112	Einführung in Python3, Bernd Klein	3	24.99
 
# Write a Python program, which returns a list with 2-tuples. Each tuple 
# consists of a the order number and the product of the price per items 
# and the quantity. The product should be increased by 10,- € if the 
# value of the order is smaller than 100,00 €. 
# Write a Python program using lambda and map.

bookShopList = [[34587, 'Learning Python, Mark Lutz', 4, 40.95], \
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],\
         [77226, 'Head First Python, Paul Barry', 3, 32.95], \
             [881122, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

# for loop solution
def getSalesTuples(shopList):
    lis = []
    for item in shopList:
        lis.append((item[0], item[2]*item[3]))
    return lis

getSalesTuples(bookShopList)

# map lambda solution
print(list(map(lambda x: (x[0], x[2]*x[3] if (x[2]*x[3])>=100 else (x[2]*x[3] + 10)), bookShopList)))


# The same bookshop, but this time we work on a different list. 
# The sublists of our lists look like this: 
# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
# Write a program which returns a list of two tuples with (order number, total amount of order).


bookShopList2 = [34587, ('Learning Python, Mark Lutz', 4, 40.95), \
    98762, ('Programming Python, Mark Lutz', 5, 56.80),\
         77226, ('Head First Python, Paul Barry', 3, 32.95), \
             881122, ('Einfuhrung in Python3, Bernd Klein', 3, 24.99)]

print(list(map(lambda x: (x if int(x[0]) else, \
    x[2]*x[3] if (x[2]*x[3])>=100 else (x[2]*x[3] + 10), bookShopList))))



# %%
