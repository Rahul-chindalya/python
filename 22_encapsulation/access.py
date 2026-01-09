# Private 
class A:
    def __init__(self,a,b):
        self.__a = a # private 
        self.__b = b # private 

obj = A(10,20)

# Accessing Private
print(obj._A__a) # Name Mangling 
print(obj.b)

#-> NOTE: Python doesn't block access to private data entirely.
#      It just leaves it to the wisdom of the programmer, not to write 
#      any code that accesses it from outside the class. 
#      You can still access the private members by Python's name mangling technique.

# -> So, is there proper encapsulation in Python?
#         Java/C++ = “You’re not allowed.”
#         Python = “You shouldn’t, but you can if you insist.”  (name mangling technique)  