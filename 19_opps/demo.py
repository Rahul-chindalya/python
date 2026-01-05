# -> Classes - Objects - Methods

# -> NOTE : When we execute, code inside class, it runs, unlike functions
# -> NOTE : Class call is not mandatory, function call is mandatory

# -> student_obj.info() # TypeError: info() takes 0 positional arguments but 1 was given

# -> NOTE: There is a default behavior with python, that is python automatically
#     passes an object (student_obj) as the first argument to the method
#         first argument is called as self 
#         self == this 

# -> NOTE : self is referring to current object of class  
#           python automatically passes self as first argument, when we call method
#           that's why methods must accept self as first parameter
#           self lets methods access instance(object) variables

# -> When we have class level variable, we can use Classname.variable to access them

# -> we have data(student_name & student_email) fixed/hard coded right in the class, 
#     now I want to pass dynamic data like we used to do in functions, then we need a 
#     special method __init__ 

# -> __init__ is a special methods(Constructor) in python

#     -> It is used to initialize the values to object variables

#     -> It will automatically run, when we create an object

#     -> When working with __init__ methods, there is no concept of return, as it always implicitly 
#     returns None 



########################################################################################################
#Student
class Student:
    # attributes 
    student_name = "ravi"
    student_email = "ravi@gmail.com"
    
    # __init__ constructor
    def __init__(self,student_name,student_email):
        return None
        return student_email
    
    # method - defined inside the class
    # def info(self):
    #     # print(self.student_name,self.student_email)
    #     print(Student.student_name,Student.student_email) # accessing with class name
        # print(student_name,student_email) # NameError: name 'student_name' is not defined
        
student_ravi_obj = Student("ravi","ravi@gmail.com")
student_krishna_obj = Student("krishna","krishna@gmail.com")
#student_obj = Student() #TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'
#print(student_obj)
#print(student_obj.student_name)
#print(student_obj.student_email)
#student_obj.info() # TypeError: info() takes 0 positional arguments but 1 was given
#Student.info() # TypeError: info() missing 1 required positional argument: 'self'

    
# define a function
def student_info():
    student_name = "krishna"
    student_email = "krishna@gmail.com"
    print(student_name,student_email)

# call func
student_info()
