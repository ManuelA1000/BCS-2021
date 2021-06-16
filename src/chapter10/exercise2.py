hour_freq = dict()
fname = input("Enter file name:\n")
try:
    handle = open(fname)
    for line in handle:
        words = line.split()
        if len(words) < 5 or words[0] != 'From':
            continue
        col_pos = words[5].find(':')
        hour = words[5][:col_pos]
        if hour not in hour_freq:
            hour_freq[hour] = 1
        else:
            hour_freq[hour] += 1
    lst = list()
    for key, val in list(hour_freq.items()):
        lst.append((key, val))
    lst.sort()
    for key, val in lst:
        print(key, val)
except FileNotFoundError:
    print("File not found.")
    quit()
