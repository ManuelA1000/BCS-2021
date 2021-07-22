fname = input('Enter the file name: ')
histogram = dict()
maximum_address = ''
maximum = 0
try:
    handle = open(fname)
    for line in handle:
        line = line.rstrip()
        #if len(line) < 2 or line[0] != 'From':
            #continue
        if line.startswith('From '):
            line = line.split()
            histogram[line[1]] = histogram.get(line[1], 0) + 1
    for key in histogram:
        if histogram[key] > maximum:
            maximum = histogram[key]
            maximum_address = key
    print(maximum_address,maximum)
except FileNotFoundError:
    print('File not found', fname)
    quit()
