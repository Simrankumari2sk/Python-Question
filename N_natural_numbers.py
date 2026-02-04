#Q. Write a program to find the sum of first N natural numbers.
print("Enter the N natural numbers: ")
N = int(input())
I = 1
sum = 0
while I <= N:
    sum = sum + I
    I = I + 1
print(f"The sum of N natural numbers is {sum}.")