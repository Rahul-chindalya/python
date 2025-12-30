# -> Exception(Error) Handling 

#     -> Exception - it's a error that occurs, during Program execution
    
#     -> What happens when an Exception occurs ?

#         -> It will abruptly stop the program execution, then and there it self

#         -> Python way of Handling Exceptions is to stop

#     -> To handle the Exceptions by yourself

#         -> try
#         -> except 
#         -> else
#         -> finally
#         -> raise 

#     -> try and except

#         -> try - code that may cause error

#         -> except - code to run if there is error


# Everything is fine, when there are no exceptions
print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")

print("="*50)

# Observe the behavior when there are exceptions -> handled by python
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
print("Program Execution Completed")
print("="*50)

# Observe the behavior when there are exceptions
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # ZeroDivisionError: division by zero   
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
    
print("Program Execution Completed")

# Observe the behavior when there are no exceptions with try and except
print("="*50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print(num1/num2) 
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
    
print("Program Execution Completed")