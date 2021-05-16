#a program that prompts the use for a list of numbers and prints maximum and minimum number
list = [] #initializing array
number = 0.0
while True:
    input_number = input("Enter a number:\n")
    if input_number == "done":
        break
    
    try:
        number = float(input_number)   
    except:
        print("invalid input ") 
        continue  
    list.append(input_number) 
if list:
    print("maximum:", max(list))       
    print("minimum:", min(list))