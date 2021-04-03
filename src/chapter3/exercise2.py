# Program to calculate the gross pay of a worker
hours_worked = input("Enter the hours worked:\n")
hourly_rate = input("Enter the payment rate:\n ")
try:  # evaluates for correct values entered, i.e numeric values
    hours = float(hours_worked)
    rate = float(hourly_rate)
except:
    print('Error, enter numerical input')
    quit()
if hours <= 40:  # calculates regular pay for 40 hours or less of work time
    Regular_pay = float((hours*rate))
    print(Regular_pay)
else:  # calculates extra pay for hour above 40 and adds up to pay for 40 hours
    above_40 = ((hours-40) * 1.5 * rate)
    Overtime_pay = (above_40 + (40 * rate))
    print(Overtime_pay)
