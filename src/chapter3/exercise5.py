# program that prompts the user to enter the number of people attending a party and prints the estimated cost
number_of_people = int(input("Enter the number of people: \n"))
if number_of_people <= 50:
    print("The wedding will cost $ 4000")
elif number_of_people <= 100:
    print("The wedding will cost $10000")
elif number_of_people <= 200:
    print("The wedding will cost $15000")
else:
    print("The wedding will cost $20000")