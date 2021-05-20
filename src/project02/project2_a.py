
try:
    with open('measles.txt', 'r') as f:
        output = input("Please enter the name of the output file:\n")
        year = input("Enter a year:\n")
        try:
            if len(year) <= 4 or year == 'all' or year == 'ALL' or year == (int(year)):
                pass
            else:
                quit("Year must be less than four characters or less characters or an integer")
        except ValueError:
            quit("Enter valid year.Thank you.")
        with open(output, 'w') as output:
            for line in f:
                f.readlines()
                if (line[:-1] == year) or (line[:-2] == year) or (line[:-3] == year) or (line[:-4] == year):
                    output.write(line)
                elif year == line[:] or year == "all" or year == "ALL":
                    output.write(line)

        print("File created successfully")

except FileNotFoundError:
    print("File not found")
    quit()