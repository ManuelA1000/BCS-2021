import string
fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
    counts = dict()
    for line in fhandle:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    print(counts)
except FileNotFoundError:
    quit('File not found')

