'''Q. Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary and house
      rent allowance is 20% of basic salary. Write a program to calculate his gross salary.'''

print("Enter the Basic Salary: ")
bs = int(input())
da = 0.4 * bs
hra = 0.2 * bs
Gross_Salary = bs + da + hra
print(f"The Basic Salary is {bs}")
print(f"The Dearness Allowance is {da}")
print(f"The House Rent Allowance is {hra}")
print(f"The Gross Salary is {Gross_Salary}")