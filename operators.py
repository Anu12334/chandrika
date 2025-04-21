#Arithmetic operators:
a = 50
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #sameas 50*50*50*50*50
print(a//b) 


#Assignment operators:

a=10
print(a)

a += 1   #a = a+1
print(a)

a -= 2
print(a)

a *= 3
print(a)

a /= 4
print(a)

a %= 5
print(a)

a //= 6
print(a)

a **= 7
print(a)

#Comparison operators:

x = 5
y = 2
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical operators:

x=20
print(x > 10 and x < 30)
print(x > 5   or x < 19)
print(not(x >25 and x < 15))

#Identity operators:

x=["chandrika","ajay"]
y=["chandrika","ajay"]
z = x
print(x is z)

print(x is y) #x and y have same values but different memory locations
print(x == y) 
 
a=(1,2,3,4)
b=(1,2,3,4)
c=b 
print(a is not c)
print(c is not b)
print(a != b) 

#Membership operators:

x=(1,2,"chandrika","ajay")
print(2 in x)
print("anuusha" not in x)


#Bitwise Operators:

