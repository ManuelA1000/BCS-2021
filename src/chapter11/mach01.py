import re
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search("^F..m:",line):
        print(line)