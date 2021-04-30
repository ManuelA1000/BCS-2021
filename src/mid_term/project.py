# program asks for billing details and calculates the water bill used in dollars
# function to calculate gallons of water used
def gallons_used(a, b):
    if b > a:
        gallons = (b-a)/10
    else:
        a = 1000000000 - a
        gallons = (a + b)/10
    print(f"Gallons of water used:{gallons}")
    return gallons


# main program starts here
while True:
    customer_code = input("Enter customer code:\n")
    initial_reading = int(input("Enter the beginning meter reading:\n"))
    ending_reading = int(input("Enter the ending meter reading:\n"))
    print(f"Customer code: {customer_code}")
    print(f"Beginning meter reading: {initial_reading}")
    print(f"Ending meter reading:{ending_reading}")
    gallons = gallons_used(initial_reading, ending_reading)
