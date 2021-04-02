# a program that prompts john's decision
location = str(input("Enter the location;\n"))
pay = int(input("Enter the pay;\n"))
if location == str('Mbarara') and pay > 4000000:
    print("Sure, I can work with this")
if location == str('Mbarara') and pay < 4000000:
    print("No Thanks, I can find something better")
elif location == str('Kampala') and pay >= 10000000:
    print("Sure, I can work with this")
elif location == str('Kampala') and pay < 10000000:
    print("no way!")
elif location == str('space'):
    print("without a doubt, i'll take it")
elif pay >= int('6000000'):
    print("sure, i can work with this")
else:
    print("No Thanks, I can find something better")
