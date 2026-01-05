#  -> MRO : Method Resolution Order

#        MRO (Method Resolution Order) in Python is the order in which 
#        Python searches for a method in a class hierarchy when multiple classes 
#        are involved (especially in multiple inheritance).
    
#         -> Rules, when you call a method on object
#             -> Python starts from the current class
#             -> Then moves left to right through base classes
#             -> Follows the MRO list of classes
#             -> Stops when it finds the first matching order 

# Method Resolution Order
class A:
    def show(self):
        print("A Show")

class B():
    def show(self):
        print("B Show")

class C(B,A):
    pass

obj = C()
obj.show()
print(C.mro())

# super()
class Parent:
    def greet(self):
        print("Hello From Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("hello from child")

child = Child()
child.greet()