'''If the marks obtained by a student in five different subjects are input through the keyboard, write a program
   to find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks
   that can be obtained by a student in each subject is 100.'''
print("Enter the marks of 5 subjects: ")
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total = m1 + m2 + m3 + m4 + m5
percentage = total/5
print(f"Aggregate Marks = {total}")
print(f"Percentage Marks = {percentage}")