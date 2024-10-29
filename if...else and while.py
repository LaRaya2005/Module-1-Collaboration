#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

#Variables
lastName = input("Student Last Name:")
while lastName !="ZZZ":
    firstName = input("Student First Name:")
    gpa = float(input(f"{lastName}'s GPA:"))
    if gpa >=3.5:
        print(f"{lastName},{firstName} made the Dean's List")
    elif gpa>=3.25:
        print(f"{lastName},{firstName} made the Honor's Roll")
    else:
        print(f"{lastName},{firstName} did not make Deans's List or Honor Roll")
        print(Enter another student's last name below")
              lastName = input("Student Last Name:")