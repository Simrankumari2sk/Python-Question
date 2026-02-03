'''The distance between two cities (in kilometers) is input through the keyboard. Write a program to convert
   and print the distance in meters, feet, inches and centimeters.'''
print("Enter the distance(in kilometers): ")
d = int(input())
m = d * 1000
cm = m * 100
inch = cm / 2.54
ft = inch / 12
print(f"Distance in meters = {m}")
print(f"Distance in centimeters = {cm}")
print(f"Distance in inches = {inch}")
print(f"Distance in feet = {ft}")