# Program to calculate the gross pay of a worker
x = int(input("Enter the hours worked:\n"))
rate = float(input("Enter the payment rate:\n "))
if x > 40:
    pay = rate*40 + 1.5*(x-40)*10
    print(pay)
if x<=40:
    pay = rate*x
    print(pay)