#Write a program to find the factorial of a number
num = int(input("Enter a number: "))
fact = 1                #fact value is taken as 1 because when it will get multiplied it will be by 1
n = 1
while n <= num:
    fact = fact * n
    n += 1
print(fact)