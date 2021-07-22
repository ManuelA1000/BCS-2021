count = 0
total = 0
name = input("Enter the name of your file:\n")
try:
    handle = open(name)
    for line in handle:
        if line.startswith('X-DSPAM-Confidence: '):
            count = count + 1
            number_pos = line.find(':')
            number = float(line[number_pos + 1:].strip())
            #print(number)
            total = number + total
    print('Average spam confidence:', total/count)
except FileNotFoundError:
    quit("Enter the correct file name,thanks.")
