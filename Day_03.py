# Zero 2 Hero (Day 03)
print("Zero 2 Hero (Day 03)")

# Use of ( if , elif , else )
#Day 03, Task 01
age = int(input("Enter your age: " ))

if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote")
    
#Day 03, Task 02
age = int(input("Enter your age to buy ticket: " ))

if age <= 10:
    print("Your ticket is free! (0Taka)")

elif age <= 25:
   print("Your ticket price is 20Taka")

else:
   print("Your ticket price is 50Taka")
   

# Input validation
age = int(input("Enter your age to buy ticket: " ))

if age < 0 or age > 120:
    print("Please enter a valid age (1-120): " )
    
elif age <= 10:
    print("Your ticket is free! (0Taka)")

elif age <= 25:
   print("Your ticket price is 20Taka")

else:
   print("Your ticket price is 50Taka")