# -> User Defined Exceptions

#     -> You can create your own Exceptions

#     -> Why ?

#         -> To handle errors in our own way, so that we can give more meaningful and readable
#         error messages

#     -> We have a predefined class called Exception

#         -> If you use(inherit) Exception class then the inherited class is User Defined Exception

#         syntax: 
#         class MyCustomException(Exception):
#             pass

class AgeTooYoungError(Exception):
    pass

class NoIDError(Exception):
    pass

# age = int(input("Enter Your Age: "))
# if age < 18:
#     raise AgeTooYoungError("You must be at least 18 years old to register")
# else:
#     has_id = input("Do you have ID ? (yes/no) ")
#     if has_id != "yes":
#         raise NoIDError("You must have an ID to register") 
# print("Registration Successful!")
# print("="*50)

try:
    age = int(input("Enter Your Age: "))
    if age < 18:
        raise AgeTooYoungError
    has_id = input("Do you have ID ? (yes/no) ")
    if has_id != "yes":
        raise NoIDError
except AgeTooYoungError:
    print("You must be at least 18 years old to register")

except NoIDError:
    print("You must have an ID to register") 
else:        
    print("Registration Successful!")
finally:
    print("Exiting Application!")   