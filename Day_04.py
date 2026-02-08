# Zero 2 Hero (Day 04)
print("Zero 2 Hero (Day 04)")

# For loop
for i in range(1, 21):
    print(f"I love you {i}")

# For loop step  
for i in range(1, 21, 2):
    print(i)
    
# For loop reverse
for i in range(20, 0, -1):
    print(i)

# While loop
i = 1
while i <= 10:
    print(f"I love you {i}")
    i = i + 1
    
#Day 04, Task 01
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")