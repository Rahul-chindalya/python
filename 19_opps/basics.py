# -> OOPS 

#     -> Object Oriented Programming

#         -> Structuring the code using OOPS principals

#         -> Here we will group data and behavior together using Objects

#         -> Why ?

#             -> Reusability

#             -> Clear Structure for Representing real world entities into programming

#             -> When we work with large scale Applications

#     -> OOPS Learning

#         -> Classes

#         -> Objects

#         -> Methods (Functions)

#         -> Inheritance

#         -> Polymorphism

#         -> Encapsulation

#         -> Abstraction         


# -> Class : Blueprint for Objects 

#     -> Laptop is a class 

#     -> Data 
#         -> Brand 
#         -> Model 
#         -> Screen
#         -> etc
    
#     -> Behavior
#         -> play_audio
#         -> play_video
#         -> etc

# -> Object : An real world instance of a class is Object, it has its own data and behavior

#     -> New Real Laptop : mac
#         -> Brand : Apple
#         -> Model : mac book air
#         -> Screen : 13 inch
#         -> etc

#         -> play_audio("can play audio with 10 watt speaker") 
#         -> play_video("can play audio with 4k Content") 

#     -> New Real Laptop : dell
#         -> Brand : Dell
#         -> Model : Alien Ware
#         -> Screen : 13 inch
#         -> etc

#         -> play_audio("can play audio with 30 watt speaker") 
#         -> play_video("can play audio with 1080p Content") 


#     -> Methods - Block of code that executes / performs a TASK / ACTION

#         NOTE - If we write a function inside a class, then it's called as Method

#         -> Methods will act on objects data i.e play_video using screen (object data)


#     -> syntaxes

#         class ClassName:
#             pass
        
#         object = ClassName()

#         def function_name():
#             pass


# class
class Laptop:
    # data -> attributes / variables 
    brand = "Apple"
    screen = 13
    
    # method
    def play_video():
        print(f"Playing Video In 4k Content")

# object
mac = Laptop()
