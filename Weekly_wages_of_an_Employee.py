'''Q. Write a program to calculate the weekly wages of an employee. The pay depends on wages per hour and the number of hour worked. Morepver,
      if the employee has worked for more than 30 hours, then he or she should gets twice the wages per hour, for every extra hour that he or
      she has worked.'''
hours_worked = int(input("Enter the hours worked by the employee: "))
wages_per_hour = int(input("Enter the wages per hour: "))
overtime_charges = 0
overtime_hours = 0
if hours_worked > 30:
    overtime_hours = hours_worked - 30
    overtime_charges = overtime_hours * (2 * wages_per_hour)
salary = (hours_worked * wages_per_hour) + overtime_charges
print(salary)