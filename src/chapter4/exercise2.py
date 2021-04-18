# program that uses a user defined function to calculate the final value of investment

def compute_investment(c, r, n, t):
    p = c*(1 + (r/n))**(t*n)
    return p


first_amount = int(input("Enter initial amount:\n"))
interest_rate = float(input("Enter the yearly rate:\n"))
compound_times = int(input("Enter the number of times interest is compounded:\n"))
years_to_mature = int(input("Enter the number of years until maturation:\n"))

compound_interest = compute_investment(first_amount, interest_rate, compound_times, years_to_mature)
print("The compound interest is", round(compound_interest, 2))
