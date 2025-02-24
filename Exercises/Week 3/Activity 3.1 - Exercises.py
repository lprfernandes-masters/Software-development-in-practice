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

# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

"""
odds, evens = 0, 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"odds: {odds}")
print(f"evens: {evens}")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V',
# "section":'A'}]

"""

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f"the var {item} is a type {type(item)}")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

"""

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')

"""

# ----------------------------------------------------------------------------------------------------------------#

# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

"""

x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x + y

"""

# ----------------------------------------------------------------------------------------------------------------#

# 10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print
# "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples
# of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz

"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""

# ----------------------------------------------------------------------------------------------------------------#


# 11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

"""

m = 3
n = 4
result = []
row = []

for i in range(m):
    for j in range(n):
        row.append(i * j)
    result.append(row)
    row = []

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#


# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

"""

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
print(lines)

"""

# ----------------------------------------------------------------------------------------------------------------#

# 13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

"""

input = "0100,0011,1010,1001,1100,1001"

values = input.split(',')
output = []

for value in values:
    if int(value,2) % 5 == 0:
        output.append(value)

print(output, sep=',')

"""

# ----------------------------------------------------------------------------------------------------------------#

"""

# 14. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

input = input()

letters = 0
digits = 0

for ch in input:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print(f"letters: {letters}")
print(f"digits: {digits}")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 15. Write a Python program to check the validity of passwords input by users.
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

"""

import re

password = input("input password")

if (re.search("[a-z]",password) and 
    re.search("[A-Z]",password) and
    re.search("[0-9]",password) and
    re.search("[$#@]",password) and
    len(password) >= 6 and
    len(password) <= 16):
        print("valid password")
else:
        print("invalid password")
        

"""

# ----------------------------------------------------------------------------------------------------------------#

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence

"""

numbers = []

for d in range(100, 401):
    if int(str(d)[0]) % 2 == 0 and int(str(d)[1]) % 2 == 0 and int(str(d)[2]) % 2 == 0:
        numbers.append(d)

print(numbers, sep=',')

"""

# ----------------------------------------------------------------------------------------------------------------#

# 17. Write a Python program to print the alphabet pattern 'A'.

"""
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
"""

"""
result = ""

for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or
            (row == 0 or row == 3) and (column > 1 and column <5)):
                result = result + "*"
        else:
             result = result + " "
    result = result + "\n"

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#

# 18. Write a Python program to print the alphabet pattern 'D'.

"""

result = ""

for row in range(0,7):
    for column in range(0,7):
        if (column == 1 or (column == 5 and (row != 0 and row != 6)) or
            (row == 0 or row == 6) and (column > 1 and column <5)):
            result = result + "*"
        else:
             result = result + " "
    result = result + "\n"

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#

# 19. Write a Python program to print the alphabet pattern 'E'.

"""

result = ""

for row in range(0,7):
    for column in range(0,7):
        if ((row == 0 or row == 3 or row == 6) and column > 0 and column < 5 or 
            column == 1):
            result = result + "*"
        else:
             result = result + " "
    result = result + "\n"

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#

# 20. Write a Python program to print the alphabet pattern 'G

"""

result = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (
            (column == 1 and row > 0 and row < 6) or
            (column == 5 and row > 0 and row < 6 and row != 2) or
            ((row == 0 or row == 6) and column > 1 and column < 5) or
            (row == 3 and column > 1 and column < 5 and column != 2)
        ):
            result = result + "*"
        else:
            result = result + " "
    result = result + "\n"

print(result)

"""

# ----------------------------------------------------------------------------------------------------------------#

# ... exercises are very similar, skipping...

# 31. Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73

"""

dog_years = int(input("Input a dog's age in human years:"))

if dog_years >= 2:
    result = round((2 * 10.5) + ((dog_years - 2) * 4))
else:
    result = round(int(dog_years * 10.5))

print(f"The dog's age in dog's years is {result}")

"""

# ----------------------------------------------------------------------------------------------------------------#


# 32. Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:
# Input a letter of the alphabet: k
# k is a consonant.

"""

vowels = ["a", "e", "i", "o", "u"]

chosen_letter = input("Input a letter of the alphabet:").lower()

if chosen_letter in vowels and chosen_letter.isalpha:
    print(f"{chosen_letter} is a vowel")
else:
    print(f"{chosen_letter} is a consonant")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 33. Write a Python program to convert a month name to a number of days.
# Expected Output:
#
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days

"""

month = input("Input the name of Month: ").lower()

if month == "february":
    print("No. of days: 28/29 days")
elif month in ("april", "june", "september", "november"):
    print("No. of days: 30 days")
elif month in ("january", "march", "may", "july", "august", "october", "december"):
    print("No. of days: 31 days")
else:
    print("month name not correct")
    
"""


# ----------------------------------------------------------------------------------------------------------------#

# 34. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

"""

first_number = int(input("please enter the first integer to sum:"))
second_number = int(input("please enter the second integer to sum:"))

total = first_number + second_number

if total >= 15 and total <= 20:
    total = 20

print(total)

"""


# ----------------------------------------------------------------------------------------------------------------#

# 35. Write a Python program that checks whether a string represents an integer or not.
# Expected Output:
# Input a string: Python
# The string is not an integer.

"""

input = input("Input a string:")

if input.isdigit():
    print("The string is an integer")
else:
    print("The string is not an integer")

"""


# ----------------------------------------------------------------------------------------------------------------#

# 36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
#
# Input lengths of the triangle sides:
# x: 6
# y: 8
# z: 12
# Scalene triangle

"""

print("Input lengths of the triangle sides:")

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x == y == z:
    print("equilateral triangle")
elif (x == y or x == z or z == y):
    print("isosceles triangle")
else: 
    print("scalene triangle")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
# Expected Output:
# Input the month (e.g. January, February etc.): july
# Input the day: 31
# Season is autumn

"""

month = input("Input the month (e.g. January, February etc.").lower()

day = int(input("Input the day:"))

if month in ("january", "february", "march"):
    season = "winter"
elif month in ("april", "may", "june"):
    season = "spring"
elif month in ("july", "august", "september"):
    season = "summer"
else:
    season = "autumn"

if (month == "march") and day > 20:
    season = "spring"
elif month == "june" and day > 20:
    season = "summer"
elif month == "september" and day > 20:
    season = "autumn"
elif month == "december" and day > 20:
    season = "winter"

print(f"Season is: {season}")

"""

# ----------------------------------------------------------------------------------------------------------------#


# same logic of the exercises from before. skipping...


# ----------------------------------------------------------------------------------------------------------------#

# 40. Write a Python program to find the median of three values.
# Expected Output
#
# Input first number: 15
# Input second number: 26
# Input third number: 29
# The median is 26.0

"""

first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
third_number = int(input("Input third number: "))

result = [first_number, second_number, third_number]
result.sort()
result = result[1]

print(f"The median is {result}")

"""

# ----------------------------------------------------------------------------------------------------------------#

# 41. Write a Python program to get the next day of a given date.
# Expected Output:

# Input a year: 2016
# Input a month [1-12]: 08
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2016-8-24

"""

import datetime

year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

result = datetime.datetime(year,month,day) + datetime.timedelta(days=1)

result_str = result.strftime("%y-%m-%d")

print(f"The next date is [yyyy-mm-dd] {result_str}")

"""

# ----------------------------------------------------------------------------------------------------------------#

#  Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

"""

total = 0

while True:
    value_input = int(input("Write a value to sum"))
    if value_input == 0:
        break
    else:
        total = total + value_input
print(f"total value is: {total}")

"""

# ----------------------------------------------------------------------------------------------------------------#

#  43. Write a Python program to create the multiplication table (from 1 to 10) of a number.

"""
Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
"""

"""

value_input = int(input("Input a number: "))

for i in range(1,11):
    print(f"{value_input} x {i} = {value_input * i}")

"""


# ----------------------------------------------------------------------------------------------------------------#


# 44. Write a Python program to construct the following pattern, using a nested loop number.
"""
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

for i in range(1, 10):
    print(str(i)*(i))
