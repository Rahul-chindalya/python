#  -> Inheritance : is a concept, where a class(subclass or child) will inherit properties and methods from
#     another class(superclass or parent). 

#     -> Purpose : Reusability

#     -> Syntax

#         class Parent:
#             pass

#         class Child(Parent):
#             pass    

#         obj = Child()

#     -> Types Of Inheritance

#         -> Single Inheritance        
#         -> Multi Level Inheritance
#         -> Multiple Inheritance
#         -> Hierarchal Inheritance
#         -> Hybrid Inheritance


# With Inheritance
class Student:
    
    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("Functionality For Watching Videos")
        print("W")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class VideoAdmin(Student):
    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("Functionality For Adding Videos")
        print("A")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50) 

class SuperAdmin(VideoAdmin):
    # video functionality deleting
    def delete_videos(self):
        print("="*50)
        print("Functionality For Deleting Videos")
        print("D")
        print("e")
        print("l")
        print("e")
        print("t")
        print("e")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50) 

# Test functionalities
print("Student User")    
student_user = Student()
student_user.watch_videos()

print("Video Admin User")    
va_user = VideoAdmin()
va_user.watch_videos()
va_user.add_videos()

print("Super Admin User")   
sa_user = SuperAdmin()
sa_user.watch_videos()
sa_user.add_videos()
sa_user.delete_videos()