# -*- coding: utf-8 -*-
"""SciAssign05BIMAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bhPTWuUfkFMG1j0OYYJdS4K73C9NOzPT

1. Write a program to convert odd numbers to even numbers in a list
"""

list = [1,3,4,5,7,9]
for i in list:
  if i % 2 != 0 :
    i = i+1
  print(i)

"""2. Write a program to replace the first element with the last and last with the first in a list."""

list = [1,2,3,4,5]
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(list)

"""3.Write a program to take user inputs and add the inputs to a list

---


"""

list = []
n = int(input("Enter the number of elements you want to add:"))
for i in range(0,n):
    element = input("Enter the element:")
    list.append(element)
print(list)

employee_records = {
    "001": "Jack",
    "002": "Jacob",
    "003": "Crystal",
    "006": "Kylie",
    "007": "Chuck",
    "0010": "Andre"
}

employee_records["0010"] = "Andrew"

employee_records["012"] = "NewEmployee1"

employee_records["004"] = "AbsentEmployee1"

employee_records.pop(2)

# Delete entire new employees record after the project is done
employee_records.clear()

print(employee_records)