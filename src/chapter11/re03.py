import re
file = input("Enter name of a file:\n")
handle = open(file)
for line in handle:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]',line)
    if len(x) > 0:
        print(x)
