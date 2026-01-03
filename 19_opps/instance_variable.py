# -> Instance Variables

#     -> Instance Variables/Attributes are variables that belong to an object (instance), not the class.
    
#     -> Instance variables are commonly defined in the __init__ method (constructor) 
#         using the self keyword
        
#     -> Each object has its own copy of instance variables with potentially different values, 
#         meaning modifying an instance variable in one object does not affect the same variable 
#         in other objects
    
#     -> Accessed via self.variable_name

# -> Instance Methods

#     -> Methods inside a class that operate on instance variables i.e 
#         Operate on object (instance) data.
    
#     -> Most common type of methods in Python classes.

#     -> Instance methods always take self as the first parameter 
#         (represents the object calling it).
    
#     -> Can access instance variables and class variables

#     -> called using object_name.method().

#     -> instance methods cannot be called with Classname

#    ->  Instance Variable + Instance Method Relationship
#             -> Instance variables store data for each object.
#             -> Instance methods use self to access & modify that data.


class Student:
    
    # Class Variable common data for all objects of student class
    institute_name = "Edify"
    
    # using constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # your methods
    def info(self):
        print("Student Institute: ",Student.institute_name) # preferred for class variables
        # print("Student Institute: ",self.institute_name) - not preferred for class variables
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)
        
# Data With Multiple Objects
student_one = Student("one","one@gmail.com") 
student_two = Student("two","two@gmail.com") 
student_three = Student("three","three@gmail.com") 

# Call your functionalities / methods
student_one.info()
student_two.info()
student_three.info()



# class Roy:
#     def __init__(self,name,last_name):
#         self.name = name.title()
#         self.last_name = last_name.title()

#     def info(self):
#         print("NAME : ",self.name)
#         print("last_name: ", self.last_name)

# one = Roy("rahul","chindalya")

# one.info()