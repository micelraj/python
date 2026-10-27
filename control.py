#a python program that checks if someone is elegible to vote

age=int(input("Enter your age:"))
if age>=18:
  print("You are elegible to vote")
else:
  print("You can't vote..underage")

#A program that checks if a number is odd or even
marks=int(input("Enter your marks :"))
if marks % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")


#create a program that checks between 3 numbers which one is the biggest
num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))
num3=int(input("Enter your third number :"))
if num1 >= num2 and num1>=num3:
  print("The largest number is:", num1)
elif num2>=num1 and num2>=num3:
  print("The largest number is:", num2)
else:
  print("The largest number is:", num3)
 

#alternate
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

largest = max(number1, number2, number3)
print("The largest number is: ", largest)