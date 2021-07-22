fname = input('Enter file name: ')
try:
    handle = open(fname)
    counts = dict()
    for line in handle:
        line = line.rstrip()
        #if line.startswith('From '):
        days = line.split()
        if len(days) < 3 or days[0] != 'From':
            continue
        elif days[2] not in counts:
            counts[days[2]] = 1
        else:
            counts[days[2]] += 1
    print(counts)
except FileNotFoundError:
    print('File not found', fname)
    quit()
"""
  Alternative way 
"""
fname = input('Enter file name: ')
try:
    handle = open(fname)
    counts = dict()
    for line in handle:
        line = line.rstrip()
        if line.startswith('From '):
            days = line.split()
            counts[days[2]] = counts.get(days[2], 0)+1
    print(counts)
except:
    print('File not found',fname)
    quit()