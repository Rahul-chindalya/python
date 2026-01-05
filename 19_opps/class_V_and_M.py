# -> Class variables

#     -> Class Variables are shared data i.e data is shared across all the instances(Objects) of class

#     -> Class Variables Belong to a class, rather than objects

#     -> Defined inside the class, but outside the methods.

#     -> Access

#         -> We can use ClassName.variable 
#         -> We can use object or self (But preferred is always classname ) 

#     -> If class variable is changed, it will reflect all the objects calling on it

#     -> For Memory efficiency, as only one copy of class variable is create, though 100's of objects
#          are using it

# -> Class Methods

#     -> Methods defined inside the class, that will operate on class variables

#     -> Not very commonly used like instance methods

#     -> Class methods are more bound to classes, but not objects

#     -> Take cls as a first parameter (cls refers as class, self refers to object) 

#     -> These methods cannot act(modify) instance data / Variables

#     -> noTE : We use @classmethod decorator for class methods

# -> Class Variable + Class Method Relationship
#     -> Class variables store data common to all objects.
#     -> Class methods change or use that shared data. 


class Student:

    #class Variable:
    institute_name = "EDIFY"

    # using constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # your methods
    def info(self):
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)
        print("Institute Name : ",Student.institute_name)
        
# Data With Multiple Objects
student_one = Student("one","one@gmail.com") 
student_two = Student("two","two@gmail.com") 
student_three = Student("three","three@gmail.com") 

# Call your functionalities / methods
student_one.info()
student_two.info()
student_three.info()
