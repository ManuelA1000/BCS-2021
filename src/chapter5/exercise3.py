# vending machine change maker programme.
print("Welcome to the vending machine change maker programme")
print("Change maker initialized")
print("Stock contains:")
print("25 nickels\n25 dimes\n25 quarters\n0 ones\n0 fives")

# requesting for price from the user
while True:

    # requesting for price input
    price = input("Enter the purchase price (xx.xx) or `q' to quit:")
    if price == "q":
        break
    item_cost = float(price)
    if (item_cost > 0) and round((item_cost*100) % 5 == 0):
        continue
    else:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
