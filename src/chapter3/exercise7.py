# a program that prompts john's decision
location = str(input("Enter the location;\n"))
pay = int(input("Enter the pay;\n"))
if location == str('Mbarara') and pay > 4000000:
    print("Sure, I can work with this")
elif location == str('Mbarara') and pay < 4000000:
    print("No thanks, I can find something better")
elif location == str('Kampala') and pay >= 10000000:
    print("Sure, I can work with this")
elif location == str('Kampala') and pay < 10000000:
    print("No way!")
elif location == str('space'):
    print("Without a doubt, I'll take it")
elif pay >= int('6000000'):
    print("Sure, I can work with this")
else:
    print("No Thanks, I can find something better")
