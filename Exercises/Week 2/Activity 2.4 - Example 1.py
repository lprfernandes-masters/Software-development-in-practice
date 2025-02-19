# Rewrite the examples above to PEP Standards.
# https://www.w3schools.com/python/python_regex.asp


# RegEx Module

import re as regex


# Search the string to see if it starts with "The" and ends with "Spain":

text = "The rain in Spain"
regex_result = regex.search("^The.*Spain$", text)


# RegEx Functions
# findall => returns a list containing all matches

regex_result = regex.findall("ai", text)
print(regex_result)


# search => returns a match object if there is a match anywhere in the string

regex_result = regex.search("\s", text)
print("The first white-space character is located in position:", regex_result.start())


# split => returns a list where the string has been split at each match

regex_result = regex.split("\s", text)
print(regex_result)


# sub => replaces one or many matches with a string

regex_result = regex.sub("\s", "9", text)  # we can pass another param count
print(regex_result)


# Match Object

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


# Looks for any words that starts with an upper case "S":

regex_result = regex.search(r"\bS\w+", text)
print(regex_result.span())


# Print the string passed into the function:

print(regex_result.string)


# Print the part of the string where there was a match.:

print(regex_result.group())
