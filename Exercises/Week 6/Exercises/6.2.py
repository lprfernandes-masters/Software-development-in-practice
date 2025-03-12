# Create and Populate a list and a dictionary. Then, serialise them to disk using pickle, and then using JSON.


import json
import pickle

my_list = list(range(1, 10))

my_dict = {"a": "1", "b": "2", "c": "3"}

"""
with open(".\Exercises\\6.2.txt", "wb") as file:
    pickle.dump(my_list, file)


with open(".\Exercises\\6.2.txt", "rb") as file:
    data_retrieved = pickle.load(file)
    print(data_retrieved)
"""

with open(".\Exercises\\6.2.txt", "w") as file:
    json.dump(my_dict, file)


with open(".\Exercises\\6.2.txt", "r") as file:
    data_retrieved = json.load(file)
    print(data_retrieved)
