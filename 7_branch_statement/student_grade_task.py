# TASK  : Student Grade Tracker
# Create a comprehensive Python program and develop a simple console-based application that tracks student grades for multiple subjects using loops, variables, data types, operators, type conversion, conditionals, and input functions. This task demonstrates how loops solve real-world problems where the quantity of data is unknown beforehand.

# Collect Student Information:
# Student ID 
# Student Name 
# Attendance 
# Number of subjects
# Total Score 
# Continue input

student_id =int(input("ENTER STUDENT ID: "))
student_name = input("ENTER YOUR NAME: ")
attendance = int(input("ENTER YOUR ATTENDENCE: "))

no_of_subjects = 0
total_score = 0

while True:
    subject_score = int(input("ENTER YOUR SCORE: "))
    total_score +=subject_score
    no_of_subjects +=1

    choice = input("U WANA ADD OTHER SCORE (yes/no): ")
    if choice != "yes":
        break

average_score = total_score/no_of_subjects

match average_score:
    case _ if average_score >= 85:
        performance = "Excellent"
    case _ if average_score >=70:
        performance = "GOOD"
    case _ if average_score >=50:
        performance = "AVERAGE"
    case _ if average_score<=50:
        performance = "NEEDS IMPORVEMENT" 

if attendance <=75:
    attandance_status ="WARNING Low Attendance"
else:
    attandance_status ="Attendance Satisfied"

print("===========================")
print("========output=============")
print("===========================")
print(f"STUDENT ID: {student_id}")
print(f"STUDENT ID: {student_name}")
print(f"TOTAL SCORE: {total_score}")
print(f"Average score : {average_score }")
print(f"PERFORMANCE : {performance }")
print(f"ATTENDANCE : {attendance }")
print(f"ATTENDANCE STATUS: {attandance_status }")
