admitted = []
not_admitted = []

def check_admission():
    print("Hello! Let's check if you're qualified for admission.")
    
    name = input("What is your name: ")
    department = input("Enter department (Computer Science/Mass Communication): ").strip().lower()
    jamb_score = int(input("What is your JAMB score: "))
    pass_interview = input("Did you pass your interview? (yes/no): ").strip().lower()
    print("Enter your grades using this reference: A = 1, B = 2, C = 3, D = 4, E = 5, F = 6")

    if department == "computer science":
        grade_eng = int(input("Grade in English Language: "))
        grade_math = int(input("Grade in Mathematics: "))
        grade_phy = int(input("Grade in Physics: "))
        grade_chem = int(input("Grade in Chemistry: "))
        grade_fmath = int(input("Grade in Further Mathematics: "))

        has_credits = (grade_eng <= 3 and grade_math <= 3 and grade_phy <= 3 and 
                       grade_chem <= 3 and grade_fmath <= 3)

        if jamb_score >= 250 and has_credits and pass_interview == "yes":
            print(f"{name} is qualified for admission into the Computer Science department.")
            admitted.append(name)
        else:
            print(f"{name} is NOT qualified for admission into the Computer Science department.")
            not_admitted.append(name)

    elif department == "mass communication":
        grade_eng = int(input("Grade in English Language: "))
        grade_math = int(input("Grade in Mathematics: "))
        grade_lit = int(input("Grade in Literature-In-English: "))
        grade_gov = int(input("Grade in Government: "))
        grade_eco = int(input("Grade in Economics: "))

        has_credits = (grade_eng <= 3 and grade_math <= 3 and grade_lit <= 3 and 
                       grade_gov <= 3 and grade_eco <= 3)

        if jamb_score >= 230 and has_credits and pass_interview == "yes":
            print(f"{name} is qualified for admission into the Mass Communication department.")
            admitted.append(name)
        else:
            print(f"{name} is NOT qualified for admission into the Mass Communication department.")
            not_admitted.append(name)
    
    else:
        print("Invalid department entered. Please choose either 'Computer Science' or 'Mass Communication'.")

while True:
    check_admission()
    cont = input("Do you want to check another candidate? (yes/no): ").lower()
    if cont != "yes":
        break

print("Admission Check Complete!")
print("Admitted candidates:", admitted)
print("Not admitted candidates:", not_admitted)
