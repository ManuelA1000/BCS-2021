# program that prompts the user to enter the number of people attending a party and prints the estimated cost

try:
    number_of_people = int(input("Enter the number of people: \n"))
    if number_of_people <= 50:
        print("The wedding will cost $ 4,000")
    elif number_of_people <= 100:
        print("The wedding will cost $10,000")
    elif number_of_people <= 200:
        print("The wedding will cost $15,000")
    else:
        print("The wedding will cost $20,000")
except ValueError:
    print('Please enter a digit\n')
