name = input("Enter the name of the file:\n")
counts = dict()
maximum = 0
maximum_address = ''

try:
    handle = open(name)
    for line in handle:
        line = line.rstrip()
        if line.startswith('From '):
            words = line.split()
            counts[words[1]] = counts.get(words[1], 0) + 1
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    value , key = lst[0]
    print(key,value)
except FileNotFoundError:
    quit("File not found.")

