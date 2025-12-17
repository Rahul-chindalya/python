print("="*30)
print("LMS GRADE TRACKING SYSTEM")
print("="*30)

student_id_valid = False
while not student_id_valid:
    student_id = input("ENTER ID: ")
    #check the given data is input
    if student_id.isdigit():
        student_id = int(student_id)
        #check  if the number is positive
        if student_id >0:
            student_id_valid = True
        else:
            print("ENTER A POSITIVE NUMBER")
    else:
        print("PLESE ENTER ONLY NUMBERS")

# print(f"STU ID :{student_id}")

instute_code= "  SMHS"
formatted_id = instute_code+"STU"+str(student_id).zfill(5)
print(formatted_id)

student_name_valid = False
while not student_name_valid:
    student_name = input("ENTER NAME: ")
    #  removing extra space and case formatting
    student_name = student_name.strip().title()
    
    #valaditation for letters and space only
    name_check =student_name.replace(" ","")

    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print(f"welcome {student_name}")
    else:
        if not name_check.isalpha():
            print("NAME SHOULD BE IN LETTERS")
        elif len(student_name) <3:
            print("NAME SHOULD BE ATLEST 3 LETTERS")

#We are simulating system generated unique email id
name_parts = student_name.split()
first_name = name_parts[0].lower()

#Generate university email: 
student_email = first_name+"."+str(student_id)+"@gmail.com"
print(student_email)

base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("ENTER BASE COURSE FEE")

    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee >0:
            base_course_fee_valid= True
        else:
            print("ENTER A POSITIVE NUMBER")
    else:
        print("ENTER ONLY NUMBERS ")

discount=0
description = input("ENTER DESCRIPTION")
description = description.lower()

if "refrence" in description:
    discount += 5000
elif "scholarship" in description:
    discount += 7000
elif "promo"in description:
    discount += 3000

final_fee = base_course_fee - discount
print("="*30)
print("FEE DETAILS")
print("="*30)

print(f"Actual Fee: {base_course_fee}")
print(f"Discount Given: {discount}")
print(f"Final Fee To Pay: {final_fee}")
