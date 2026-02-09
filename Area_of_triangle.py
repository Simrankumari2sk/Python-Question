#Q. Write a program to write area of the triangle using Heron's formula.
a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
S = (a + b + c) / 2
Area =(S * (S - a) * (S - b) * (S - c)) ** 0.5          #Heron's formula
print("The area of the triangle is", Area)