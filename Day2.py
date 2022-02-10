# assignment a
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


def isPalindrome(string):
    new_string = string.lower()
    new_string = new_string.translate(str.
                maketrans('','', string.punctuation))
    if new_string == new_string[::-1]:
        return [True if new_string ==  else False]


result = ['Y' for x in phraseList if isPalindrome(x) else 'N']
# result = phraseList

print(result)



# assignment b
# %%
