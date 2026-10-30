#1 List datasctruture
#Changeable/mutable
#ordered, indexex
myproducts=["Bread", "Milk","Sugar","Blueband"]
print(myproducts)
myproducts.pop()
myproducts[1]="honey"
print(f"I like drinking tea that has {myproducts[1]}")
print(myproducts)


#2 Tuple datastructures
#ordered has indexes
#Unchangeable
countrys=("Kenya", "Tanzania", "Burundi","Somalia","Rwanda")
print(countrys)

#3 Set Datastructres
#Avoids duplicates
#Unordered
computers={"hp","Lenovo", "Dell", "hp"}
print(computers)

#4 Dictionary datastructures
customer= {
  "name":"Kalii",
  "Age":25,
  "City":"Nairobi",
  "Salary": 300000,
  "Professional":"Software Engineer"
}
print(f"Customer Name: {customer['name']}")

myfruits=["mangoes", "oranges", "pineapples", "watermelon", "avocado"]

for m in myfruits:
  print(f"I have {m}")

#imagine you are building a 
#schhol system that calculates the average marks
marks=[65,89,64,89,90]
total=0
for x in marks:
  total=total+x
average=total / len(marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")

#Create a comples calculator 
# using inputoutput and controlflows
print("Operations: +, -, *, /, %, **")

# loop to keep calculator running
while True:
    
    operator = input("Enter operator (+,-,*,/,%,**) or 'q' to quit: ").lower()

    if operator == "q":
        print("Calc terminated")
        break

    # --- TWO NUMBER OPERATIONS ---
    if operator in ["+", "-", "*", "/", "%", "**"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            elif operator == "%":
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif operator == "**":
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


    else:
        print("Invalid operator! Try again.")