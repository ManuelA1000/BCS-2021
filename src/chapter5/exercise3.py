# vending machine change maker programme.
# function that has menu for selection of bill/money to be deposited
def selection_menu():
    print("Menu for deposits")
    print("'n'- deposit a nickel\n'd' - deposit a dime\n'q' - deposit a quarter\n"
          "'o' - deposit a one dollar bill\n'f' - deposit a five dollar bill"
          "\n'c' - cancel the purchase")


def amount_due(price):
    total_cents = round(price*100)
    dollars = total_cents // 100
    cents = total_cents % 100
    print("Payment due: ", dollars, "dollars and ", cents, "cents")


def balance(amount_deposited, item_cost):
    print("Take the change below:")
    change = amount_deposited-item_cost
    change = round(change*100)
    while change >= 25:  
        print(change//25, "quarter(s)")
        change = change % 25
        continue
    while change >= 10: 
        print(change//10, "dime(s)")
        change = change % 10
    while change >= 5:  
        print(change//5, "nickel(s)")
        break
    else: 
        print("0 cents")


def enter_deposit():
    amount_due(item_cost)
    amount_deposited = 0
    while item_cost > amount_deposited:
        deposit = input("Indicate your deposit")
        if deposit == "c":
            break

    
# main programme starts off here
print("Welcome to the vending machine change maker programme")
print("Change maker initialized")
print("Stock contains:")
n = 25
d = 25
q = 25
o = 0
f = 0
print(f"{n} nickels\n{d} dimes\n{q} quarters\n{o} ones\n{f} fives")
# requesting for price from the user
while True:
    try:
        # requesting for price input
        price = input("Enter the purchase price (xx.xx) or `q' to quit:")
        if price == "q":
            break
        item_cost = float(price)
        if (item_cost > 0) and round((item_cost * 100) % 5 == 0):
            selection_menu()
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
    except:
        print("Input can't be rendered, please enter a non-negative multiple of 5 cents ")
