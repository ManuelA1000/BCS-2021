word = 'achom elvin'
d = dict()
for letter in word:
    word.rstrip()
    d[letter] = d.get(letter, 0) + 1
print(d)
