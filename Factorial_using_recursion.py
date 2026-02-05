#Q. Write a program to find the factorial of a number using recursion.
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter a number: "))
if n <= 0:
    print("Factorial for the number less than 1 does not exist.")
else:
    print("Factorial of",n,"is", fact(n) )