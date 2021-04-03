# program that computes 1.5 times more the hourly rate for workers who work for more than 40 hours
hours_worked = input('Enter the hours worked:\n')
hourly_rate = input('Enter the hourly rate:\n')

hours = float(hours_worked)   # converting the user input to float for hours worked
rate = float(hourly_rate)     # and hourly rate
if hours <= 40:
    Regular_pay = (hours * rate)
    print(Regular_pay)
else:
    Overtime_pay = ((40*rate) + ((hours-40)*1.5*rate))         # 1.5times the rate for every hour worked
                                                               # overtime is computed and added to regular pay
    print(Overtime_pay)
