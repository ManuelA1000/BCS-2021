# a program that lets John enter his pay and location then evaluates his decision
location = input("Enter the location;\n")
pay = int(input("Enter the pay;\n"))
if location == 'Mbarara' and pay > 4000000:
    print("Sure, I can work with this")
elif location == 'Mbarara' and pay < 4000000:
    print("No thanks, I can find something better")
elif location == 'Kampala' and pay >= 10000000:
    print("Sure, I can work with this")
elif location == 'Kampala' and pay < 10000000:
    print("No way!")
elif location == 'space':
    print("Without a doubt, I'll take it")
elif pay >= 6000000:
    print("Sure, I can work with this")
else:
    print("No Thanks, I can find something better")
