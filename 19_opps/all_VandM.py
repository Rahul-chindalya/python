
#     -> Instance Variables
#     -> Class Variables
#     -> Instance Methods
#     -> Class Methods
#     -> Static Method
#     -> Local Variables


# -> Static Methods - Not bound to either the class or object, 

#     -> So static methods do not depend on instance variables nor class variables

#     -> It's not ver often used

#     -> For some helper functions or utilities can be Static Methods

#     -> We use @staticmethod decorator

#     -> For static methods, it's not mandatory to pass first argument like cls or self


# -> Local Variable

#     -> Variable whose scope only exist within the methods
#     -> student_name,student_email as parameters are local variables


class Student:

    #class Variable:
    institute_name = "EDIFY"

    

    # Instance method constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # y methods
    def info(self):
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)
        print("Institute Name : ",Student.institute_name)

    #class method
    @classmethod
    def change_Instute(cls,new_name):
        cls.institute_name=new_name

    #static Method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
    
    #local variable
    var = 20
    print(var)

# Data With Multiple Objects
student_one = Student("one","one@gmail.com") 
student_two = Student("two","two@gmail.com") 
student_three = Student("three","three@gmail.com")

Student.change_Instute("EDIFY LMS")

print(Student.validate_email("onegmail"))

# Call your functionalities / methods
student_one.info()
student_two.info()
student_three.info()