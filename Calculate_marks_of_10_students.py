'''Q. Write a program to read the marks of 10 students. If the marks is greater than 50 the students passes, else the student fails. Count
      the number of students passing or failing.'''
student_pass = 0
student_fail = 0
no_of_students = 1
while no_of_students <= 10:
    marks = int(input("Enter the marks of the student: "))
    if marks >= 50:
        student_pass = student_pass + 1
    else:
        student_fail = student_fail + 1
    no_of_students = no_of_students + 1
print("The total no. of students passed =", student_pass)
print("The total no. of students failed =", student_fail)