# #a python program that checks if someone is elegible to vote

# age=int(input("Enter your age:"))
# if age>=18:
#   print("You are elegible to vote")
# else:
#   print("You can't vote..underage")

# #A program that checks if a number is odd or even
# marks=int(input("Enter your marks :"))
# if marks % 2 == 0:
#   print("The number is even")
# else:
#   print("The number is odd")


# #create a program that checks between 3 numbers which one is the biggest
# num1=int(input("Enter your first number :"))
# num2=int(input("Enter your second number :"))
# num3=int(input("Enter your third number :"))
# if num1 >= num2 and num1>=num3:
#   print("The largest number is:", num1)
# elif num2>=num1 and num2>=num3:
#   print("The largest number is:", num2)
# else:
#   print("The largest number is:", num3)
 

# #alternate
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# number3 = float(input("Enter the third number: "))

# largest = max(number1, number2, number3)
# print("The largest number is: ", largest)

# #create a program that performs addition, subtraction, multiplication, and division of two numbers based on user input.
# #When declaring variable make sure you declare them as float to handle decimal numbers and operator as a variable i.e operator = input("Enter the operator (+, -, *, /)")

# number1=float(input("Enter your first number :"))
# number2=float(input("Enter your second number :"))

# operator=input("Enter operator(+, -, *, /): ")
# if operator=="+":
#   print(f"The sum is {number1+number2}")
# elif operator=="-":
#   print(f"The difference is {number1-number2}")
# elif operator=="*":
#   print(f"The multiplication is {number1*number2}")
# elif operator=="/":
#   if number2 !=0:
#     print(f"The quotient is {number1/number2}")
#   else:
#     print("You cannot divide by zero")
# else:
#   print("invalid operator")

# #GRADE STUDENTS MARKS
# #use the following grading system to grade students marks 70 and above = A, 60-69 = B, 50-59 = C, 40-49 = D, below 40 = Fail
# marks=float(input("Enter your Marks: "))
# if marks<0 or marks>100:
#   print("Invalid Marks")
# elif marks>=70:
#   print("A")
# elif marks>=60 and marks<=69:
#   print("B")
# elif marks>=50 and marks<=59:
#   print("C")
# elif marks>=40 and marks<=49:
#   print("D")
# else:
#   print("Fail")




#ELECTRICITY BILL CALCULATOR
#WRITE A PROGRAM THAT CALCULATES THE ELECTRICITY BILL BASED ON THE NUMBER OF UNITS CONSUMED. THE BILLING RATES ARE AS FOLLOWS:
#- For the first 100 units: 25 per unit
#- For the next 100 units (101-200): 35 per unit
#- For the next 100 units (201-300): 45 per unit

units=float(input("Enter your units: "))
if units <=100 and units >=0:
  bill=units*25
elif units>=101 and units<=200:
  bill=units*35
elif units>=201 and units<=300:
  bill=units*45
else:
  print("Invalid units")
print(f"Your electricity bill is: {bill}")