# #simple if statement
# age=18
# if age >= 18:
#     print("You are eligible to vote")
#if-else statement
# password = "hello123"
# if password == "hello123":
#     print("Access granted")
# else: 
#     print("Access denied")
#if-elif-else statement
# jamb_score=int(input("Enter your jamb score: "))
# if jamb_score <= 200:
#     print ("your admission is not guaranteed")
# elif jamb_score >= 200 and jamb_score <= 250:
#     print("your admission into the faculty of Mathematical science is guaranteed")
# elif jamb_score >= 250 and jamb_score <= 300:
#     print("your admission into the faculty of Engineering is guaranteed")
# elif jamb_score >= 300 and jamb_score <= 400:
#     print("your admission into the faculty of Medicine is guaranteed")
# else:
#     print("Try again, your score is invalid")
# #A simple calculator
# number_1 = int(input("Value: "))
# operator = input("Enter an operator (+, -, *, /): ")
# number_2 =int(input("value: "))
# if operator== "+":
#     print(number_1 + number_2)
# elif operator== "-":
#     print(number_1 - number_2)
# elif operator== "*":
#     print(number_1 * number_2)
# elif operator== "/":
#     print(number_1 / number_2)
# else:
#     print("Invalid operator")
#neste if i.e if inside if
Jamb_score=int(input("enter your jamb score: "))
if Jamb_score<=250:
    print ("Excellence")
    if Jamb_score>=300:
        print("Distinction")
        if Jamb_score<=400:
            print("First Class")
        


