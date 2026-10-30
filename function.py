def greet():
  print("This is my first function")
greet()

# function with parameters
def student(name,age,course):
  print(f"Student name is {name}")
  print(f"Student age is {age}")
  print(f"Student course is {course}")
student("Kalii",24,"Statistics")
student("Sharlene", 20, "Python")
student("Kelvin", 25, "Stata")
student("Bree", 19, "Django")

# function with return keyword
def add_number(a,b):
  return a+b
result=add_number(6,26)
print(f"Sum :{result}")

def product_number(num1,num2):
  return num1*num2
output=product_number(8,9)
print(f"Product :{output}")