# If statement:
a = 20
b = 10
if a > b:
    print("a greater than b")

#if-else Statement:
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

#if-elif-else Statement     

x=5
if x>5:
    print("x is greater than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")

#Nested if Statement:

x=10
if x>5:
    if x < 15:
        print("x is between 5 and 15")

#match statement:   
day = 4

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")


#looping statement:

#for loop:
for i in range(1,10):
    print(i)

# while loop:

i = 5
while i <= 10:
    print(i)
    i += 1 

# break example

for i in range(10):
    if i == 5:
        break
    print(i)  # Stops when i == 5

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)  # Skips 2

# pass example
for i in range(3):
    pass  # No action, just a placeholder

