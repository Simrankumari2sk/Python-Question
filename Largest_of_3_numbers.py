#Q. Write a program to find the largest among the three given number.
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
if A > B:
    if A > C:
        print(f"The largest number is {A}")
    else:
        print(f"The largest number is {C}")
else:
    if B > C:
        print(f"The largest number is {B}")
    else:
        print(f"The largest number is {C}")