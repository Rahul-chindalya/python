# Client program, trying to use my_module
import custome_module

# client trying to give his own data
name = "krishna"
email = "krishna@gmail.com"

print(custome_module.name)
print(custome_module.add(20,30))
print(custome_module.info(name,email))

print(custome_module.info_new(name="ram",email="ram@gmail.com"))