# -> Exception Handling

#     -> When we get multiple Exceptions

#     -> If you want to know appropriate types of errors, we can use sys module

#         -> sys.exc_info() 

#     -> To catch multiple Exceptions, you can use multiple except's

#     -> else & finally

#         -> else - Runs if no Exception is raised in the try block 

#         -> finally - Runs no matter what happens, whether you have an Exception or not
#             -> For finally cleaning up 

# Multiple Types Of Exceptions
import sys
list_data = [1,2,'Python',0,5,6]
for i in list_data:
    try:
        print(1/i)
    except:
        print(sys.exc_info())
        print("OOPS! Something went wrong")
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print("Program Execution Completed")
print("="*50) 

# Multiple Types Of Exceptions
import sys
list_data = [1,2,'Python',0,5,6]
for i in list_data:
    try:
        print(1/i)
    except TypeError:
        print("OOPS! Don't divide Strings with numbers")
    except ZeroDivisionError:
        print("OOPS! Don't divide numbers with zero")
print("Program Execution Completed")
print("="*50)  

# else block -> runs if no exception
print("="*50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print(num1/num2) 
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful!!! proceeding with further steps")
finally:
    print("Program Execution Completed")
print("="*50)

