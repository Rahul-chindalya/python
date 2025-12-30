#   -> Working with Web Applications

#         -> Interaction happens between Client and Server

#     -> JSON is light weight data interchange format

#     -> Working with JSON is must when using Web Development API's 

#         -> Django 

#     -> We Can import json module and work with JSON data

#     -> When Working With json module

#         -> json.dump() -> Write JSON to file

#         -> json.load() -> Read JSON from file

#         -> json.dumps() -> Convert Python To String 

#         -> json.loads() -> Convert String To Python


# Work with JSON data 
import json

student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

print(type(student))

# writing python data to json file
with open("student.json","w") as file:
    json.dump(student,file,indent=4)

#reading json file and keeping in python data format
with open("student.json","r") as file:
    print(type(file))
    py_data = json.load(file)
print(type(py_data))
print(py_data)
print("welcome:" ,py_data["name"])

# Directly using data instead of files -> write
student_json = json.dumps(student,indent=4)
print(type(student_json))
print(student_json)

# Directly using data instead of files -> read
student_json_data = json.loads(student_json)
print(type(student_json_data))

#working with web app simulation
with open("users.json","r") as file:
    data = json.load(file)
    filter_data=[]
    for user in data['users']:
        if user["age"] < 30:
            filter_data.append(user['username'])
print(filter_data)

with open("filtered_data","w") as file:
    json.dump(filter_data,file,indent=4)