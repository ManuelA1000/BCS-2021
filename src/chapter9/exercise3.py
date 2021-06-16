fname = input('Enter the file name: ')
try:
    handle = open(fname)
    histogram = dict()
    for line in handle:
        line = line.rstrip()
        if line.startswith('From '):
            line = line.split()
            histogram[line[1]] = histogram.get(line[1], 0) + 1
    print(histogram)
except FileNotFoundError:
    print('File not found', fname)
    quit()
