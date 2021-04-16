# program that computes 1.5 times more the hourly rate for workers who work for more than 40 hours and otherwise pay for work less than 40
hours_worked = input('Enter the hours worked:\n')
hourly_rate = input('Enter the hourly rate:\n')

try:
    hours = float(hours_worked)  # converting the user input to float for hours worked
    rate = float(hourly_rate)  # and hourly rate
except:
      print("Enter a numerical input\n")
      quit()
if hours > 40:  
    Regular_pay = (hours * rate)  # calculating pay for 40 hours or below
    Extra_pay = ((hours - 40) * 0.5 * rate)  # calculating pay for extra hours
    Overtime_pay = Regular_pay + Extra_pay
    print(Overtime_pay)
else:
    Normal_pay = hours * rate  # computing pay for normal work time
    print(Normal_pay)


