# we shall start by openning the file that contains the text that we want to use
with open('measles.txt' , 'r') as f:
    year = input("Enter year:\n")
for line in f:
        line = line.upper()
        year = line[-5:]
        if year.startswith (year):
            print(line)
        elif year == "all" or year == "ALL" or year == " ":
            print(f)   
        else:
            print("invalid input , try again later")    
             
    