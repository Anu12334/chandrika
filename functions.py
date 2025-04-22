def greet(name):  #Defining a function
    print("hello",name)  # Using arguments

greet("chandrika") #Calling the function

def add(a,b): # function with return
    return a + b

result = add(10, 5)
print("Sum:", result)

#Default Parameters:

def greet(name = "guest"):
    print(f"hello,{name}")

greet()
greet("chandu")

# Keyword Arguments:

def student_infor(name,age):
    print(f"name:{name},age:{age}")
student_infor(age=24,name="chandrika")

#Arbitrary Arguments (*args, **kwargs)

def total(*numbers):
    print("Sum:", sum(numbers))

total(1, 2, 3, 4)  


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Calling the function
print_details(name="Ravi", age=25, city="Hyderabad")


#Return Multiple Values:

def calculator(x, y):
    return x + y, x - y, x * y

add, sub, mul = calculator(5, 2)
print("Add:", add, "Sub:", sub, "Mul:", mul)


 #Lambda function:

x = lambda a: a + 10  
print(x(5))

a = lambda a,b :a*b
print(a(5,10))

square=lambda x:x*x
print(square(4))  


# Recursion (Function calling itself)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
