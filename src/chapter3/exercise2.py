# Program to calculate the gross pay of a worker
hours_worked = input("Enter the hours worked:\n")
rate = input("Enter the payment rate:\n ")
try:
    pay = int(hours_worked) * float(rate)
    print(pay)
except hours_worked:
    print("Error, please enter numerical input")
