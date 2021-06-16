handle = open('mbox-short.txt')
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        print(words[2])


