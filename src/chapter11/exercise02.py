import re
file = input("Enter file:")
count = 0
sum = 0
try:
    handle = open(file)
    for line in handle:
        line = line.rstrip()
        lst = re.findall('^New .*: ([0-9.]+)',line)
        count += 1
        for i in lst:
            sum = sum + int(i)
    print(count)
    print(sum)
    print(sum/count)
except FileNotFoundError:
    quit("Enter correct file name.")