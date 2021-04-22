## group1BCS1 MEMBERS
#1.ASHABAHEBWA ABDULSWABUR  2020/BCS/023/PS
#2. ACAR EMMANUEL 2020/BCS/011/PS
#3. OGONGA CHRISTOPHER 2020/BCS/008
#4. MUJUNI SHEM 2020/BCS/083/PS
#5. SSEMPEWO ROGERS 2020/BCS/077/PS
# vending machine change maker program
a = ["25 nickles" ,"25 dimes" , "25 quarters" , "0 ones " , "0 fives"] # a list of stock 
print("Welcome to the vending machine change maker program:") ;print("Change maker initialized:")
for i in a:
    print(i)
while True:
    price =input("Enter the purchase price (xx.xx) or `q' to quit:\n")
    try:
        price  = float(price)
        if price < 0 and price%0.05 != 0:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
        else:
            print("Menu for deposits")
            menu = ["'n' - deposit a nickel" , "'d' - deposit a dime" , "'q' - deposit a quarter" ,
                    "'o' - deposit a one dollar bill" ,"'f' - deposit a five dollar bill" ,
                    "'c' - cancel the purchase"]      
            for deposit in menu:
                print(deposit) 
            price = int(price*100)    
            dollars = price//100 
            cents = price%100
            x = "Payment due:"
            y = "dollars and"
            z = "cents"
            print( x , str(dollars) , y , str(cents) , z)           
    except:
        price = "q"
        continue
     
    

    
    