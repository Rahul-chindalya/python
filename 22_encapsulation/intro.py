# Encapsulation
# -> Encapsulation : Binding Data and Behavior together inside a class and 
#     restricting(not very strict in python) direct access to data. 

# -> Languages like C++?Java, they use access modifiers which is for strict enforcing 

# -> Python uses naming conventions to implement Encapsulation

# -> Python supports three types 

#     -> Public : Accessible from anywhere, both inside and outside the class

#     -> Private : Accessible only within the class, we use __(double) (prefix)
       
#     -> Protected : Accessible within the class and subclass, we use _(single) (prefix)

#     -> NOTE : Private inside python is not truly private, just hard to access
############################################################################################
#     -> NOTE: Python doesn't block access to private data entirely.
#      It just leaves it to the wisdom of the programmer, not to write 
#      any code that accesses it from outside the class. 
#      You can still access the private members by Python's name mangling technique.

#     -> So, is there proper encapsulation in Python?

#         Java/C++ = “You’re not allowed.”
#         Python = “You shouldn’t, but you can if you insist.”  (name mangling technique)  


#     -> NOTE : Encapsulation in python is achieved using

#         -> Naming conventions use __prefix (private)
#         -> Using Controlled Validations for data
#             -> Using @property(python way) or regular getter & setters
##########################################################################################
# Public 
class A:
    def __init__(self,a,b):
        self.a = a # public 
        self.b = b # public 

obj = A(10,20)

# Accessing Public
print(obj.a)
print(obj.b)

# Protected 
class A:
    def __init__(self,a,b):
        self._a = a # Protected 
        self._b = b # Protected 

obj = A(10,20)

# Accessing Protected
print(obj.a)
print(obj.b)

# Private 
class A:
    def __init__(self,a,b):
        self.__a = a # private 
        self.__b = b # private 

obj = A(10,20)

# Accessing Private
print(obj.a)
print(obj.b)
