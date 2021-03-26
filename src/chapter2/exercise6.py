# This program prompts the user to enter two points A(x1,y1) and B(x2,y2),
# and calculates the distance between them
x1 = int(input('Enter x1:\n'))
x2 = int(input('Enter x2:\n'))
y1 = int(input('Enter y1:\n'))
y2 = int(input('Enter y2:\n'))
distance = ((((x2-x1)**2) + ((y2-y1)**2))**0.5)

print('The distance between the two points is', distance)
