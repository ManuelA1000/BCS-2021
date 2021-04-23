# program that reads user input and prints total, count and
count = 0
total = 0

while True:
    try:
        number = input("Enter a number:")
        if number == "done":
            break
        num1 = int(number)
        count = count+1
        total = total+num1
    except:
        print("Invalid input")
        continue

print(total, count, total/count)