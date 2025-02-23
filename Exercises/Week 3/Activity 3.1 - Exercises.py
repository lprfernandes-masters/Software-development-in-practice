# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


"""
numbers = []
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        numbers.append(n)

print("1 - " + str(numbers))
print("")

"""

# ----------------------------------------------------------------------------------------------------------------#


# 2 . Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

""" 

temp = input("Write the temp you want to convert => 45F, 102C, etc")

units = temp[-1].lower()
degrees = int(temp[:-1])

if units == "c":
    result = round(degrees * 9 / 5 + 32)
    units = "f"
elif units == "f":
    result = round((degrees - 32) * 5 / 9)
    units = "c"
else:
    raise TypeError("units not recognized")

print(f"2 - {result}{units}")
print("")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well
# guessed!" message, and the program will exit.

"""

import random
number_chosen = 0
number_to_guess = random.randrange(1, 10)

while number_chosen != number_to_guess:
    number_chosen = int(input("Choose a number between 1 and 10"))

print("Well guessed")

"""

# ----------------------------------------------------------------------------------------------------------------#


""" 4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*



for i in range(1, 6):
    print(i * "* ")

for i in range(4, 0, -1):
    print(i * "* ")

    
"""


# ----------------------------------------------------------------------------------------------------------------#

# 5. Write a Python program that accepts a word from the user and reverses it.

"""

result = ""
word = input("choose a word to reverse it: ")

for i in range(len(word) - 1, -1, -1):
    result = result + word[i]

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#
