dictionary = dict()
handle = open('words.txt').read()

words = handle.rstrip().split()
#words = handle.split()
for i in words:
    dictionary[i] = 'anything'
    print(dictionary)


if 'a' in dictionary:
    print("yes")