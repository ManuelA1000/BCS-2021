import re
file = input("Enter file name:\n")
RE = input("Enter a regular expression.")
command = 'RE\S.*'
count = 0
try:
    handle = open(file)
    for line in handle:
        line = line.rstrip()
        lines = re.findall(command,line)
        count = count +1
    print(count)

except FileNotFoundError:
    quit("Enter correct file name.")