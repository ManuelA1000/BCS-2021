import re

file = input("Enter file name:\n")
try:
    handle = open(file)
    for line in handle:
        lst = re.findall('^X\S*: ([0-9.]+)', line)
        if len(lst) > 0:
            print(lst)
except FileNotFoundError:
    quit("File not found.")
