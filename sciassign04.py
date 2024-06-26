# -*- coding: utf-8 -*-
"""SciAssign04BIMAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sATYt6u8gr9aRUaBzDVaCv34Gx-L9NDw

:Aarush recently learned probability in his school. He was finding the probability of different events and he wondered whether he can develop a program to do the same thing or not. To help Aarush create a program in python where user can enter number of favorable outcomes and total number of possible outcomes and then program will print the probability of that event on the screen. ● Note: ● Print the probability of the event only up to 2 decimal places. ( For this use round() function ) ● Sample run ● >>Enter the number of favorable outcomes: 1 ● >>Enter the total number of possible outcomes: 2 ● >>Probability: 0.5
"""

favoutcomes = int(input("Enter the number of favorable outcomes: "))
totaloutcomes = int(input("Enter the total number of possible outcomes: "))

probability = favoutcomes / totaloutcomes

roundedprobability = round(probability, 2)

print("Probability:", roundedprobability)

"""2:The RTO (Regional Transport Office) website holds a registration form which is responsible for registering a user for a Driving License. The RTO wants to take the next step if and only if the user's age is greater than or equal to 18.
So write a program in python to help the RTO find out whether the registered user's age is greater than or equal to 18 or not.

"""

age = int(input("Enter your age: "))
if age >= 18:
  print("Eligible for Driving lisence")
else:
  print("Not eligible for Driving lisence")

"""Scarlet, a fifteen year old, wants to be creative and is inspired by watching alexa, siri, google on how they act as smart chatbots and assistants and wanted to create her own chatbot. So write a program in python using the if-else, Nested if-else, if-else-if ladder where ever necessary.
The Bot Has the Behave in following manner
Step 1: ask the user for his/her name.
Step 2: wish the user by telling his name For Ex: Hi My name is Jenni, chatbot. A Very Good Day To You username!!.
Step 3: How are you feeling today??(Based on what user entered you are suppose to respond if user entered good statement then say something positive like."It's really a productive day to do something innovative and you are close to it. "If the user says something negative then respond accordingly and try to cheer him up.

"""

name = input("Enter your name: ")
print(f"Hi my name is scarlet, chatbot. A very good day to you {name}!!")
feeling = input("How are you feeling today?? [Good/Bad]")
if feeling == "good":
  print("It's really a productive day to do something innovative and you are close to it. ")
elif feeling == "bad":
  print("Cheer up! Don't worry!! you got this username!!. buckle up and cheer yourself up. Good days are on their way. There is no beautiful rainbow without a heav")
else:
  print("I don't understand what you mean. Can you try rephrasing your answer (between good/bad)?")

"""Sir Osborne Smith is a Governor who takes care of Reserve Bank Of India, his son Rahul Smith, a 15 year old, was learning coding being a Governor of RBI Sir Osborne wanted to test the coding skills of Rahul Smith and asked him to write a python code for an ATM machine. But Rahul is confused with few of the concepts.
So write a python code to explain how an ATM machine code works and to explain the concepts to Rahul
bank_balance = 50000
The ATM Machine should be having the following options:
1) Withdraw : Withdraw amount that are multiples of 100 like 100, 200, 1000, 2000 and so onNote: throw error if user enters numbers like 111, 112, 781,etc as 1 rupees, 2 rupees, 10 rupees, 50 rupees are impossible in ATM2) Deposit Cash3) Balance Enquiry : Show the
Account Balance4) Fast Cash : where there will be options on the screen like 5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000 and the user can just select any one option so.

"""

bank_balance = 50000

while True:
  print("------------------------------------------------------------------------------------------------")
  print("Enter 1 for Withdraw")
  print("Enter 2 for Deposit")
  print("Enter 3 for Balance Enquiry")
  print("Enter 4 for Fast Cash")
  print("Enter 5 to exit")

  option = int(input("Enter your option: "))

  if option == 1:
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    if withdraw_amount % 100 != 0:
      print("Please enter an amount that is a multiple of 100.")
    elif withdraw_amount > bank_balance:
      print("Insufficient funds.")
    else:
      bank_balance = bank_balance - withdraw_amount
      print("Your balance is now", bank_balance)
  elif option == 2:
    deposit_amount = int(input("Enter the amount to deposit: "))
    bank_balance = bank_balance + deposit_amount
    print("Your balance is now", bank_balance)
  elif option == 3:
    print("Your balance is", bank_balance)
  elif option == 4:
    fast_cash_amount = int(input("Enter the amount to withdraw: "))
    if fast_cash_amount in [5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]:
      bank_balance = bank_balance - fast_cash_amount
      print("Your balance is now", bank_balance)
    else:
      print("Please enter an amount that is a valid fast cash option.")
  elif option == 5:
    break
  else:
    print("Invalid option.")

"""Jack, a 19 year old, has learnt python. He has written a code using python that will literally accept color names as an input from the user and prints all of the colors. Jack is still thinking of a logic and whenever the color is red hence he wrote a if condition inside a for loop but the compiler started throwing an error stating that if condition cannot be left empty.
So write a python program to help Jack to keep his if condition empty temporarily and print rest of the colors using a for loop

"""

colors = ["red", "green", "blue", "yellow", "orange", "purple", "black", "white", "pink", "brown"]

for color in colors:
  if color == "red":
    pass
  else:
    print(color)

"""Yash and Vishal have invested 10000$ in their bank. Yash is getting 6% simple interest from his bank and Vishal is getting 6% compound interest from his bank. Write a python program to calculate the difference in their returns after 30 years. What is the difference in their return in one year? What is the reason for this difference? Discuss ● Hint: Use the following parameters to calculate interest ● Principal amount ● Time ● Rate of interest"""

principal = 10000
rate = 6/100
time = 30

simple_interest_yash = principal * rate * time
compound_interest_vishal = principal * (1 + rate) ** time
total_yash = principal + simple_interest_yash
difference = compound_interest_vishal - simple_interest_yash


print("simple intrest of YASH after 30 years =>",simple_interest_yash)
print("after 30 year the total amount YASH will have is =>",total_yash)
print("compaund intrest of VISHAL after 30 years =>",round(compound_interest_vishal,2))
print("after 30 year the amount VISHAL will have is =>",principal + round(compound_interest_vishal,2))
print("-------")
print("The difference in returns after 30 years is =>", round(difference,2))
print("The difference in returns in one year is:", round(difference/time,2))
print("Reason:-\n    The reason for the difference is that compound interest is calculated on the principal amount plus the interest that has been earned in previous years \n    while simple interest is calculated only on the principal amount.")

"""**Nidhi**'s father is not able to calculate his annual tax correctly. He is a bit confused with the taxation rule also each year his total annual income is different. So to help her father Nidhi decides to write a python program that can calculate the tax to be paid based on annual income. Write the same program to calculate the tax to be paid based on annual income. ● Hint: take the annual income as input from the user and print the amount of tax to be paid. These are tax rules."""

income = float(input("Enter your annual income: "))

if income <= 250000:
  tax = 0
elif income <= 500000:
  tax = (income - 250000) * 0.05
elif income <= 750000:
  tax = (income - 500000) * 0.10
elif income <= 1000000:
  tax = (income - 750000) * 0.15
elif income <= 1250000:
  tax = (income - 1000000) * 0.20
elif income <= 1500000:
  tax = (income - 1250000) * 0.25
else:
  tax = (income - 1500000) * 0.30


final_tax = tax - tax * (0.10)
print("Your tax to be paid is:", tax)

"""Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write a program in python to check your BMI by putting your height and weight as input. ● Note: ● Body Mass Index is a simple calculation using a person's height and weight. The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most adults 18-65 years.

"""

weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in meter:"))
BMI=weight/height**2


if BMI >= 25.0:
  print(f" Your BMI is {BMI} : overweight")
elif BMI <= 24.9 and BMI>=18.5:
  print(f'Your BMI is {BMI} : Healthy')
else:
  print("Under weight please eat")

"""A year consists of 365 days. But once in every four years, it consists of 366 days. And that is known as a leap year. Shisha wants to know whether the current year is a leap year or not. She found that any year divisible by 4 is a leap year, if the year is divisible by 100 then it will not be a leap year, and if the year is divisible by 400 then it will be a leap year. Write a program in python to check whether the given year is a leap year or not to help Shisha. ● Hint: Use if elif else condition"""

year=int(input("enter a year:"))
if year%100==0:
  if year%400==0:
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")
elif year%4==0:
   print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

