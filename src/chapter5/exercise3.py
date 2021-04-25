# Vending Machine Change Maker
# Vending Machine Change Maker
## GROUP1BCS1 MEMBERS
#1. ASHABAHEBWA ABDULSWABUR  2020/BCS/023/PS
#2. ACAR EMMANUEL 2020/BCS/011/PS
#3. OGONGA CHRISTOPHER 2020/BCS/008
#4. MUJUNI SHEM 2020/BCS/083/PS
#5. SSEMPEWO ROGERS 2020/BCS/077/PS
print("Welcome to the Vending Machine Change Maker Program")
print("Change maker initialized.")
stock_list = ["25 nickles" ,"25 dimes" , "25 quarters" , "0 ones " , "0 fives"]
for i in stock_list:
    print(i)
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

price = input("Enter the purchase price (xx.xx) or 'q' to quit:\n ")

while price != 'q':
    price_n = float(price)
    total_cents = round(price_n * 100)
    dollars = total_cents // 100
    cents = total_cents - (dollars * 100)

    if total_cents % 5 == 0 and total_cents > 0:
        print("Menu for deposits")
        menu = ["'n' - deposit a nickel" , "'d' - deposit a dime" , "'q' - deposit a quarter" ,
                "'o' - deposit a one dollar bill" ,"'f' - deposit a five dollar bill" ,
                 "'c' - cancel the purchase"]
        for deposit in menu:
            print(deposit)
        print("Payment due: ", dollars, "dollars and ", cents, "cents")
        deposit = input("Indicate your deposit: ")

        while total_cents > 0:
            if deposit.isdigit() == False:
                if deposit == 'n':
                    total_cents -= 5
                    nickels += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit == 'd':
                    total_cents -= 10
                    dimes += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit == 'q':
                    total_cents -= 25
                    quarters += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit == 'o':
                    total_cents -= 100
                    ones += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit == 'f':
                    total_cents -= 500
                    fives += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit == 'c':
                    break
                else:
                    print("Illegal deposit: ", )
                if total_cents > 0:
                    print("\nPayment due: ", dollars, "dollars and ", cents, "cents")
                    deposit = input("Indicate your deposit: ")
                else:
                    if total_cents == 0:
                        print("\nPlease take the change below.\n   No change due.")
                        break
                    change_quarters = abs(total_cents) // 25
                    if change_quarters > quarters:
                        change_quarters = quarters
                        quarters = 0
                    else:
                        quarters -= change_quarters
                    total_cents += change_quarters * 25
                    change_dimes = abs(total_cents) // 10
                    if change_dimes > dimes:
                        change_dimes = dimes
                        dimes = 0
                    else:
                        dimes -= change_dimes
                    total_cents += change_dimes * 10
                    change_nickels = abs(total_cents) // 5
                    if change_nickels > nickels:
                        change_nickels = nickels
                        nickels = 0
                    else:
                        nickels -= change_nickels
                    total_cents += change_nickels * 5
                    print("\nPlease take the change below.\n  ", change_quarters, "quarters\n  ", change_dimes,
                          "dimes\n  ", change_nickels, "nickels")
                    if total_cents < 0:
                        dollars = abs(total_cents) // 100
                        cents = abs(total_cents) - (dollars * 100)
                        print("Machine is out of change.\nSee store manager for remaining change.\nAmount due is: ",
                              dollars, "dollars and", cents, "cents.")
                    break
            else:
                print("Illegal deposit: ", deposit)
                deposit = input("\nIndicate your deposit: ")

    else:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        stock_list = ["25 nickles" ,"25 dimes" , "25 quarters" , "0 ones " , "0 fives"]
        for i in stock_list:
            print(i)
        price = input("Enter the purchase price (xx.xx) or 'q' to quit:\n ")

print("Thank You for using the Vending Machine Change Maker Program")







