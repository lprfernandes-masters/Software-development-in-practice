
"""
with open(".\Exercises\source_text.txt", "r") as reader:
    print(reader.readlines())

with open(".\Exercises\source_text.txt", "a") as writer:
    writer.write("....and such...")

import os

os.rename(".\Exercises\source_text.txt", ".\Exercises\source_text_renamed.txt")


import os

script_dir = os.getcwd()

for root, dirs, files in os.walk(script_dir):
    print(f"\nCurrently looking at: {root}")
    print("Subdirectories:", dirs)
    print("Files:", files)

"""
