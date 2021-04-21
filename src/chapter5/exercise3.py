# vending machine change maker program
a = ["25 nickles", "25 dimes", "25 quarters", "0 ones ", "0 fives"]  # a list of stock
print("Welcome to the vending machine change maker program:")
print("Change maker initialized:")
for i in a:
    print(i)
while True:
    price = input("Enter the purchase price (xx.xx) or `q' to quit:\n")
    try:
        price = float(price)
        if price < 0 and price % 0.05 != 0:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
        else:
            print("Menu for deposits")
            menu = ["'n' - deposit a nickel", "'d' - deposit a dime", "'q' - deposit a quarter",
                    "'o' - deposit a one dollar bill", "'f' - deposit a five dollar bill", "'c' - cancel the purchase"]
            for deposit in menu:
                print(deposit)
    except:
        price = "q"
        continue





