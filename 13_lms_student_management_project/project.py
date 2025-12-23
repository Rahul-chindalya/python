# Create a Student Management System that allows administrators (like functionality) to manage student records including their scores and skills. The system should demonstrate practical usage of all four Python data structures.
#    Part 1: System Setup
#      1. Create system information which is fixed and shouldn’t be modified 
#         System name: "LMS Students Portal"
#         Version: "v1.0"
#         Year: "2025"
#         Institution: "Edify University"
SYSTEM_INFO =("LMS Student Portal","v1.0","2025","Edify University")
ADMIN_INFO = ("admin@edify","101","+91-8899774455")

#      2. Create admin contact information which shouldn’t be modified 
#         Email, Phone, and Room number
#      3. Create appropriate data structures for 1 & 2
#      4. Display system info at the start
print("*"*50)
print(f"Wlecome to {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
print(f"Developred By {SYSTEM_INFO[2]} In The Year{SYSTEM_INFO[3]}")
print("*"*50)

# Create an appropriate data structures to store all students
# Student ID (string)
# Student details

# Part 2: Core Features to Implement
#   Feature 1: Add Student
#   Prompt for Student ID and check if it already exists
#   Get student name and format it properly (capitalize each word)
#   Store multiple scores
#   Accept scores one by one until user types 'done'
#   Validate that scores are integers between 0-100
#   Store unique skills
#   Accept skills one by one until user types 'done'
#   Automatically handle duplicates
#  
#   Feature 2: Modify Student Name
#      Search for student by ID 
#      Update the name if student exists
#      Show appropriate error message if student not found
#      ID shouldn’t be updated
# 
#   Feature 3: Delete Student
#      Remove student record by ID
#      Show confirmation message
#      Handle when student ID doesn't exist
# 
#   Feature 4: List All Students
#      Display all student information in a formatted way
#      For each student show:
#      ID and Name
#      All scores 
#      Average score 
#      Highest score 
#      All skills 

student = {}

while True:
    print("1-Add Student")
    print("2-Modify student")
    print("3-Delete Student")
    print("4-List all students")
    print("5-Exit")

    choice = input("ENTER YOUR CHOICE [1-5]: ")
    if choice == "1":
        print("Performing Choice 1")
        student_id = input("ENTER STUDENT ID: ")
        if student_id in student:
            print("Student ID Already Exists")
        else:
            name = input("Enter STUDENT NAME").strip().title()
            scores=[]
            while True:
                score_input = input("ENTER YOR SCORE OR TYPE DONE: ")
                if score_input =="done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0<=score <=100:
                        scores.append(score)
                    else:
                        print("ENTER BETWEEN 0-100 ONLY")
                else :
                    print("Enter Only Numbers")
            skills = set()
            while True:
                skill_input = input("ENTER YOUR SKILLS OR ENTER DONE: ")
                if skill_input =="done":
                    break
                else:
                    skills.add(skill_input.strip().title())
            student[student_id]={
                "name" : name,
                "skills": skills,
                "scores": scores
            }
            print("Student ADDED SUCCESSFULLY")
            print(student)

    elif choice =="2":
        print("Performing Choice 2")
        student_id = input("Enter student id to modify: ")
        if student_id in student:
            new_name = input("ENTER New Name: ").strip().title()
            student[student_id]["name"] = new_name
            print("Student Updated Successfully")
            print(student)
        else:
            print("enter a valid student id")

    elif choice =="3":
        print("Performing Choice 3")
        student_id = input("Enter student id to modify: ")
        if student_id in student:
            removed = student.pop(student_id,None)
            print("student deleted successfully")
            print(student)
        else:
            print("enter a valid id")

    elif choice == "4": 
        print("Performing Choice 4")
        if not student:
            print("NO STUDENT AVALILABLE ")
        else:
            print("All Students Information")
            for sid,data in student.items():
                name = data["name"]
                score = data["scores"]

                if score:
                    avg =sum(score)/len(score)
                else:
                    avg = 0
                if score:
                    top_score = max(score)
                else:
                    top_score = 0
                
                skills = data["skills"]
                print(f"ID: {sid}")
                print(f"Name: {name}")
                print(f"Scores: {scores}")
                print(f"Average Score: {avg}")
                print(f"Top Score: {top_score}")
                print(f"Skills: {skills}")
                print(f"Skills Count: {len(skills)}")
    elif choice == "5":
        print("Performing Choice 5")
        print("*"*50)
        print("Contact admin for help")
        print(f"mobile number{ADMIN_INFO[2]}")
        print(f"Email {ADMIN_INFO[0]}")
        print("*"*50)
        break 
    else :
        print("ENTER A VALID NUMBER FROM [1-5]")
