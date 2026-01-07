# Polymorphism

    # -> Polymorphism : Many Forms for single entity 

    #     -> Same method, with different behaviors, depending on object calling
    
    # -> Overriding : In python, when a sub class provides custom implementation for
    #     parent class method, then this concept is called method Overriding.

    # -> Duck Typing :  
    #     "If it walks like a duck and it quacks like a duck, then it must be a duck." 
    #     -> No Inheritance is required, just methods name is enough

class Dog:
    def speak(self):
        print ("Dog Woof")

class Cat:
    def speak(self):
        print("Cat Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

#Function Polimorphism
# Pre defined - use cases for Polymorphism
print(len("hello"))
print(len([1,2,3]))
print(len({"a":1,"b":2}))

# Based On Operators (Operator Overloading)
print(2 + 3)
print("Hi" + " how are you")
print([1,2] + [3])

# common use case functionality
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 5 * 5
    
def print_area(shape):
    print("Area", shape.area())

print(print_area(Circle()))    
print(print_area(Square()))   

# Real Word Use Case - Database Connection
class MySQL:
    def connect(self):
        return "Connected To MySQL"

class PostgresSQL:
    def connect(self):
        return "Connected To PostgresSQL"

def open_db_connection(db):
    print(db.connect())

open_db_connection(MySQL())
open_db_connection(PostgresSQL())

# Method Overloading - not accepted in python
class MathOps:
    def add(self,a,b):
        return a + b

    def add(self,a,b,c):
        return a + b + c

add_obj = MathOps()
#print(add_obj.add(2,3)) # TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(add_obj.add(2.2,3.4,2))