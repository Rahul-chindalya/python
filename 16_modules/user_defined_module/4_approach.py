# Loading Modules -> Name Shadowing
from custome_module import name,email
from other_Custome_module import name,email

print(name)
print(email)

print(name)
print(email)

#so to solve the issue follow 5th approach 4 apprach is not practically usefully as it gets confused.
