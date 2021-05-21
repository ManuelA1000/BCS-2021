# program reading portions of a file based on year entered
try:
    with open('measles.txt', 'r') as f:  # opening file to read from
        output = input("Please enter the name of the output file:\n")
        year = input("Enter a year:\n")
        try:
            if len(year) <= 4:
                pass
            else:
                quit("Year must be less than four characters or less characters or an integer")
        except ValueError:
            quit("Enter valid year.Thank you.")
        with open(output, 'w') as output:
            for line in f:
                if line[88:92].startswith(year):
                    output.write(line)
                elif year == line[:] or year == "all" or year == "ALL":
                    output.write(line)

        print("File created successfully")

except FileNotFoundError:
    print("File not found")
    quit()
