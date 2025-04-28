#class and Object:

class animal:      #class
    def sound(self):
        print("animals make sounds")

dog = animal()  #Create Object
dog.sound()

# __init__ method Define Attributes

class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute
    
    def introduce(self):  # Method (functions that perform actions)
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("chandrika", 24) # Create Object

person1.introduce() # Call Method



#Inheritance:

# 1.Single Inheritance:

class animal:       # Parent class
    def speak(self):
        print("amimal speaks")

class Dog(animal): # Child class
    def bark(self):
        print("Dog barks") 

dog = Dog() # Create an object of Dog class

dog.speak()  # Calling method from Parent class

dog.bark()   # Calling method from Child class

# Multilevel Inheritance :

class Animal: # Parent class
    def eat(self):
        print("Animal eats")

class Mammal(Animal): # Child class
    def walk(self):
        print("Mammal walks")

class Dog(Mammal): # Grandchild class
    def bark(self):
        print("Dog barks")

dog = Dog() # Create an object of Dog class


dog.eat() # Calling method from Grandparent class
   
dog.walk() # Calling method from Parent class
  
dog.bark() # Calling method from Child class
  
# Hierarchical Inheritance :

class Animal:  # Parent class
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Child class 1 
    def bark(self):
        print("Dog barks")

class Cat(Animal): # Child class 2
    def meow(self):
        print("Cat meows")

dog = Dog() # Create objects of Dog and Cat classes
cat = Cat()


dog.speak()  # Calling method from Parent class (Animal) 
cat.speak() 
  

dog.bark()  # Calling methods from Child classes  
cat.meow()   

# Multiple Inheritance:

class Father: # Parent class 1
    def skills(self):
        print("Father: Gardening")

class Mother:  # Parent class 2
    def talents(self):
        print("Mother: Painting")

class Child(Father, Mother): # Child class (inherits from both Father and Mother)
    def play(self):
        print("Child plays games")

child = Child() # Create an object of Child class

child.skills()   # Calling methods from both Parents  
child.talents()   

child.play()   # Calling method from Child class    


# overriding:

class Animal: # Parent class
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal): # Child class
    def sound(self):  # Overriding the parent method
        print("Dog barks")

dog = Dog() # Create an object of Dog class

dog.sound()  # Call the sound method
  
