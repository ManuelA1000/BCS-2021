# program that asks for billing details and calculates the water bill used in dollars
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
    if customer_code == "r" or customer_code == "R":
        initial_reading = int(input("Enter the beginning meter reading:\n"))
        ending_reading = int(input("Enter the ending meter reading:\n"))
        if 0 <= initial_reading <= 999999999 and 0 <= ending_reading <= 999999999:
            print(f"Customer code: {customer_code}")
            print(f"Beginning meter reading: {initial_reading:09d}")
            print(f"Ending meter reading:{ending_reading:09d}")
            gallons = gallons_used(initial_reading, ending_reading)
            bill = 5 + (0.0005 * gallons)
            print(f"Amount billed: ${bill:.2f}")
        else:
            print("Invalid entry")
    elif customer_code == "c" or customer_code == "C":
        initial_reading = int(input("Enter the beginning meter reading:\n"))
        ending_reading = int(input("Enter the ending meter reading:\n"))
        if 0 <= initial_reading <= 999999999 and 0 <= ending_reading <= 999999999:
            print(f"Customer code: {customer_code}")
            print(f"Beginning meter reading: {initial_reading:09d}")
            print(f"Ending meter reading:{ending_reading:09d}")
            gallons = gallons_used(initial_reading, ending_reading)
            if gallons <= 4000000:
                bill = 1000
            else:
                bill = 1000 + (gallons - 4000000) * 0.00025
            print(f"Amount billed: ${bill:.2f}")
        else:
            print("Invalid entry")
    elif customer_code == "i" or customer_code == "I":
        initial_reading = int(input("Enter the beginning meter reading:\n"))
        ending_reading = int(input("Enter the ending meter reading:\n"))
        if 0 <= initial_reading <= 99999999 and 0 <= ending_reading <= 999999999:
            print(f"Customer code: {customer_code}")
            print(f"Beginning meter reading: {initial_reading:09d}")
            print(f"Ending meter reading:{ending_reading:09d}")
            gallons = gallons_used(initial_reading, ending_reading)
            if gallons <= 4000000:
                bill = 1000
            elif 4000000 < gallons <= 10000000:
                bill = 2000
            else:
                bill = 2000 + (gallons - 10000000) * 0.00025
            print(f"Amount billed: ${bill:.2f}")
        else:
            print("Invalid entry")
    else:
        print("Invalid customer code")
        break
