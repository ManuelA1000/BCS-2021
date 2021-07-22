import re
file = input("Enter name of your file:\n")
try:
    handle = open(file)
    for line in handle:
        line = line.rstrip()
        if re.search('^X\S.+: [0-9.]+', line):
            print(line)
except FileNotFoundError:
    quit('Enter correct file name.')
