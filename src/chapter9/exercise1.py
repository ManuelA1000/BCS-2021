store = dict()
fhand = open('words.txt')
count = 0
words = fhand.read().split()
for i in words:
    count += 1
    if i in store:
        continue
    store[i] = count
print(store)

if 'is' in store:
    print('True')
else:
    print('False')