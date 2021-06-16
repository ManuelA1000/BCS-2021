mail = dict()
fname = input("Enter the file name:\n")
try:
    handle = open(fname)
    for line in handle:
        line = line.split()
        words = line
        if len(words) < 2 or words[0] != 'From':
            continue
        else:
            atpos = words[1].find('@')
            domain = words[1][atpos + 1:]
            if domain not in mail:
                mail[domain] = 1
            else:
                mail[domain] += 1
    print(mail)
except FileNotFoundError:
    print("Enter correct file name.")
    quit()