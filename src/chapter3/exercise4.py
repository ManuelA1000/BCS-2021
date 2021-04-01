# program that shows eligibility to vote basing on age
voter_age = int(input("Please enter your age: \n"))
if voter_age >= 18:
    print("You can vote.")
elif voter_age == 0 and voter_age <= 17:
    print("You are too young to vote")
elif voter_age < 0:
    print("You are a time traveller")
