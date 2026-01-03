
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