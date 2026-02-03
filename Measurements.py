'''Q. The length and breadth of a rectangle and radius of a circle are input through the keyboard. Write a
   program to calculate the area and perimeter of the rectangle, and the area and circumference of the circle.'''
print("Enter the length and breadth of the Rectangle: ")
length = int(input())
breadth = int(input())
area_of_the_rectangle = length * breadth                 #Formula to calculate the area of the rectangle
perimeter_of_the_rectangle= 2 * length + 2 * breadth         #Formula to calculate the perimeter of the rectangle
print(f"The area and perimeter of the Rectangle is {area_of_the_rectangle} and {perimeter_of_the_rectangle}.")
print("Enter the radius of the circle: ")
radius = int(input())
area_of_the_circle = 3.14 * radius * radius             #Formula to calculate the area of the circle
circumference_of_the_circle = 2 * 3.14 * radius         #Formula to calculate the circumference of the circle
print(f"The area and circumference of the Circle is {area_of_the_circle} and {circumference_of_the_circle}.")