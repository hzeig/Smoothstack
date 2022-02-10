#%% 1.
a = 50 + 50
b = 100 - 10
print(a, '\n', b)


#%% 2.
print((30+6))
30*6
6^5
0b1101
1*2**0 + 0*2**1 + 1*2**2 + 1*2**3
6**6
6+6+6+6+6+6


#%% 3.
print("hello world")
print("Hello World: 10")


#%% 4. Mortgage Calculator
# Formula: M = P((r*((r+1)**N))/((1+r)**N)-1)
# M = mortgage
# P = principal / loan size
# r = monthly interest rate
# N = number of payments / length of time to pay out
import math

loanSize = input("Enter loan size:")
interestRate = input("Enter yearly interest rate:")
lengthTime = input("Enter payment period in months:")
P = float(loanSize)
r = (float(interestRate)*.01)/12
N = float(lengthTime)
M = P*((r*((r+1)**N))/(((r+1)**N)-1))
print("Your monthly mortgage is","${:,}".format(math.ceil(M)))

# %%
