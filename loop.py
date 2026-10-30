#for loop

for i in range(1,11):
  print(f"Welcome to my shop!Customer {i} ")
customers=["Kalii", "Mwongeli","Mike", "Shee", "Bree", "Obash", "Alex", "Beth"]

for c in customers:
  print(f"Welcome to todays class! {c} ")

#calculate expense that i bought
# bread ksh90
# milk ksh110
# sugar ksh170
my_shopping=[90,120,160]
total=0
for m in my_shopping:
  total=total+m
print(f"My total shopping cost is {total}")

#imagine you have five customer and each pay you 100. 
#create a script to get the total

total=0
for num in range(1,6):
  total=total+100
print(f"Total money collected : ksh {total}")

#while loop
x=0
while x<=10:
  print(f"Loops {x}")
  x+=1

#imagine you want to save starting 0 balance and save 100 daily until you have 1000
money=0
while money<1000:
  money=money+100
  print(f"Money saved: {money}")
print("Congratulations! you have reached your target")


