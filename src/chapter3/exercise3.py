# program that lets a user enter their score and returns their grade
try:
    score = float(input("Enter your score: "))
    if 0.90 <= score <= 1.0:
        print("A")
    elif 0.80 <= score <= 0.89:
        print("B")
    elif 0.70 <= score <= 0.79:
        print("C")
    elif 0.60 <= score <= 0.69:
        print("D")
    elif 0.0 <= score <= 0.59:
        print("Fail")
    else:
        print("Bad Score")
except ValueError:
    print("Kindly enter the score between 0.0 to 0.9")
