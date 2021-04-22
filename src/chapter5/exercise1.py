# a program that prompts the user to enter numbers until done, then compters the average
num = 0
tot = 0.0
while True:
    number = input("Enter a number:\n")
    if number == "done":
        break
    try:
        num1 = float(number)
    except:
        print("invalid input")
        continue
    num = num+1
    tot = tot + num
print("all done")
print(tot,num ,tot/num)