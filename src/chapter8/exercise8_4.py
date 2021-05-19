
my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()                # Splits line into array of words
    for word in words:
        if word in my_list:
            continue                    # Discards duplicates
        my_list.append(word)            # Updates the list
print(sorted(my_list))                  # Alphabetical order
