# program that lets a user enter their score and returns their grade
try:
    score = float(input("Enter your score: "))
    if score >= 0.90 and score <= 1.0:
        print("A")
    elif score >= 0.80 and score <= 0.89:
        print("B")
    elif score >= 0.70 and score <= 0.79:
        print("C")
    elif score >= 0.60 and score <= 0.69:
        print("D")
    elif score >= 0.0 and score <= 0.59:
        print("Fail")
    else:
        print("Bad Score")
except:
    print("Kindly enter the score between 0.0 to 0.9")
