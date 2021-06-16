count = 0
name = input("Enter the name of your file:\n")
try:
    if name == 'na na boo':
        print("NA NA BOO TO YOU -  You have been punk'd")
        pass
    else:
        handle = open(name)
        for line in handle:
            if line.startswith('Subject:'):
                count += 1
        print('There were ', count, 'subject lines in ', name)
except FileNotFoundError:
    print('File cannot be opened:',name)
