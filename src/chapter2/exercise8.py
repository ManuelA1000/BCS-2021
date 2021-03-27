# program that prompts the user for input and calculates the compound interest

C = int(input('Enter the initial amount:\n'))
r = float(input('Enter yearly rate:\n'))
t = int(input('Enter the number of years till maturation:\n'))
n = int(input('Enter the number of times the interest is compounded:\n'))

P = C*((1 + (r/n))**(t*n))
print('The final value of investment is', round(P, 2))
