'''Q. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this
   temperature into Centigrade degrees.'''
print("Enter the Temperature in Fahrenheit: ")
temp = int(input())
#Formula of converting from fahrenheit to celsius: subtract by 32, multiply by 5 and divide by 9.
sub = temp - 32
mul = sub * 5
div = mul / 9
celsius = div
print(celsius)