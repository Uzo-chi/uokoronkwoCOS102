def checkCompScience(name, admitted, not_admitted):
    pass_grades = ["A", "B", "C"]
    score = int(input("What was your JAMB score? "))
    s1 = input("\nWhat grade did you get in your Mathematics WASSCE? ")
    s2 = input("What grade did you get in your English WASSCE? ")
    s3 = input("What grade did you get in your Physics WASSCE? ")
    s4 = input("What grade did you get in your Chemistry WASSCE? ")
    s5 = input("What grade did you get in your Computer Science WASSCE? ")
    iview = input("\nDid you pass the interview? (Enter y/n): ")
    
    if iview == 'y':
        interview = "Pass"
    else:
        interview = "Fail"
    
    grades = [s1,s2,s3,s4,s5]
    
    details = {
                'name': name.title(), 'math': s1.upper(),
                'english': s2.upper(), 'physics': s3.upper(),
                'chemistry': s4.upper(), 'computer': s5.upper(),
                'jamb': score, 'interview': interview
            }
    
    if score >= 250 and interview == "Pass":
        for grade in grades:
            if grade.upper() not in pass_grades:
                not_admitted.append(details)
                return
            else:
                continue
        admitted.append(details)
    else:
        not_admitted.append(details)
            
    
def checkMassComm(name, admitted, not_admitted):
    pass_grades = ["A", "B", "C"]
    score = int(input("What was your JAMB score? "))
    s1 = input("\nWhat grade did you get in your Mathematics WASSCE? ")
    s2 = input("What grade did you get in your English WASSCE? ")
    s3 = input("What grade did you get in your Literature WASSCE? ")
    s4 = input("What grade did you get in your Government WASSCE? ")
    s5 = input("What grade did you get in your Economics WASSCE? ")
    iview = input("\nDid you pass the interview? (Enter y/n): ")
    
    if iview == 'y':
        interview = "Pass"
    else:
        interview = "Fail"
    
    grades = [s1,s2,s3,s4,s5]
    
    details = {
                'name': name.title(), 'math': s1.upper(),
                'english': s2.upper(), 'literature': s3.upper(),
                'government': s4.upper(), 'economics': s5.upper(),
                'jamb': score, 'interview': interview
            }
    
    if score >= 230 and interview == "Pass":
        for grade in grades:
            if grade.upper() not in pass_grades:
                not_admitted.append(details)
                return
            else:
                continue
        admitted.append(details)
    else:
        not_admitted.append(details)

admitted = []
not_admitted = []

print("These are the options for the available courses:")
print("1. Computer Science\n2. Mass Communication")

while True:
    name = input("\nWhat is your name? (Enter 'q' to quit): ")
    
    if name == 'q':
        break
    else:
        choice = input("Where would you like to enroll? (Enter 1 or 2): ")

        if choice == '1':
            checkCompScience(name,admitted,not_admitted)
        elif choice == '2':
            checkMassComm(name,admitted,not_admitted)
        else:
            print("\nUnavailable!")
            continue

if admitted:
    print("\nDetails of admitted students:")
    for admit in admitted:
        print(admit)

if not_admitted:
    print("\nDetails of non-admitted students:")
    for n_admit in not_admitted:
        print(n_admit)