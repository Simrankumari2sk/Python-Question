#Q. Write a program to print the grade obtained by a student.
print("Enter the marks: ")
mark = int(input())
if mark > 75:
    print("Grade = A")
elif mark <= 75 and mark > 60:
    print("Grade = B")
elif mark <= 60 and mark > 50:
    print("Grade = C")
elif mark <= 50 and mark > 40:
    print("Grade = D")
else:
    print("Grade = O")