# -*- coding: utf-8 -*-
"""ClassWork01BIMAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ezX4fInZqSekqiXxcD9kQkkti8Q4i6Ey

Robert, a 14 year old kid wanted to create a really cool game where he had to guess a random number that is generated, there would be only 10 chances to guess the exact number. So write a python program that randomly picks up a number in a given range and accepts the input from the user and checks if its the same as random number picked if yes the prints the user is the winner else print you loose
"""

import random
number = random.randint(1,10)
for i in range (10):
  guess= int(input("guess the number"))
  if i < 9:
    if guess == number:
      print("win!!!!!!!")
      break
    elif guess > number:
      print("guess a smaller number")
    else:
      print("guess a larger one")
  else:
    print("you lose")

print("Welcome to the Adventure Game!")
print("You are standing outside of your house, and you see a man running towards you, asking for urgent shelter.")
choice1 = input("Will you provide shelter to him? (Yes / No)\n").lower()
if choice1 == "yes":
        print("\nAfter 2 minutes, the Police came to your house and asked if the thief was in your house or not.")
        choice2 = input("Will you say 'Yes' or 'No'?\n").lower()
        if choice2 == "yes":
            print("\nYou are an honest person. He was a thief. Congratulations, you won the game!")
        elif choice2 == "no":
            print("\nYou helped a thief. Game over!")
        else:
            print("\nInvalid input. Please enter 'Yes' or 'No'. Game over!")
elif choice1 == "no":
  print("\nYou chose not to provide shelter. The man runs away. The game ends.")
else:
  print("\nInvalid input. Please enter 'Yes' or 'No'. Game over!")

words = ['school', 'books', 'friends', 'maths', 'parents', 'zoology', 'games', 'television', 'space', 'rocket', 'chemistry', 'house', 'studies', 'project']

print("Welcome to the Jumbled Words Game!")
print("Try to unscramble the word and type your guess. If you want to quit, type 'quit'.")

while True:
  word_to_guess = random.choice(words)
  shuffled_word = list(word_to_guess)
  print(shuffled_word)
  random.shuffle(shuffled_word)
  shuffled_word = ''.join(shuffled_word)

  print(f"\nJumbled word: {shuffled_word}")

  user_guess = input("Your guess: ").lower()

  if user_guess == 'quit':
    print("Thanks for playing! Goodbye.")
    break
    if user_guess == word_to_guess:
      print("Congratulations! You guessed it right. You get 1 point!")
    else:
      print("Oops! Wrong guess. Try again.")

"""1. Write a program to perform intersection and complement operation on a set
without using inbuilt functions
"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Intersection
intersection_set = set()
for elem in set1:
  if elem in set2:
    intersection_set.add(elem)

print("Intersection:", intersection_set)

# Complement
complement_set = set()
for elem in set1:
  if elem not in set2:
    complement_set.add(elem)



print("Complement:", complement_set)

"""2. Write a program to store subject wise details of 5 students of the same class
using nested dictionaries
"""

student_details = []
for i in range(5):
  student = {}
  student["name"] = input("Enter student name: ")
  student["age"] = int(input("Enter student age: "))
  student["subjects"] = {}
  for j in range(3):
    subject = input("Enter subject name: ")
    marks = int(input("Enter marks: "))
    student["subjects"][subject] = marks
  student_details.append(student)

print(student_details)

"""3:Consider these two Sets, A={19,34,56,7} B={1,2,5,19,34,7}. Write a program to
implement union operation without using inbuilt function.
"""

set1 = {19, 34, 56, 7}
set2 = {1, 2, 5, 19, 34, 7}
result_set = set()
for elem in set1:
  result_set.add(elem)
for elem in set2:
  result_set.add(elem)
print(result_set)

"""Part-1
● In a school a teacher was assigning questions for homework to the students. The
teacher randomly selected some textbook exercise questions and told students
to note the question number. Rohit wanted to solve all the questions in order but
he had written question numbers in random order. To help Rohit in arranging the
question numbers in ascending order, write a program in python that takes
different numbers as input given by the user and print it in ascending order.

● Hint:
● Take the input from the user and store the numbers in a list.
● Sort the list using nested for loops.
● Note: Don’t use the inbuilt sort function/method to sort the list.
● Sample run:

● >> Enter total number of questions: 4
● >> Enter question numbers here:
● >>23
● >>7
● >>15
● >>3
● >>Selected questions are: [ 23,7,15,3 ]
● >>Selected questions in order: [ 3,7,15,23 ]

Part-2
● Rohit was not able to solve a few questions given by his teacher. But still he
wanted to maintain the order of solving questions. He thought of leaving the
pages for those questions that he is not able to solve. So now he wants to know
the page number where he has to write the solution to a specific question.
( Assume page number starts from 1 ). To help Rohit in this modify the existing
program so that it can take the question number as input and can print page
number for that question


● Hint:
● Search for the question in the list and print index+1 on the screen.
● Example:
● If Selected questions in order is [ 3,7,15,23 ] ( same as above )
● Then, sample run
● >> Enter the question number: 15
● >> Solve it on page number 3.
● .
● Note: If question number is not available in the list then print
● >> you don’t have to solve this question.
"""

total_questions = int(input("Enter total number of questions: "))
questions = []
for i in range(total_questions):
    question_number = int(input("Enter question numbers here: "))
    questions.append(question_number)
print("Selected questions are:", questions)

for i in range(total_questions):
    for j in range(i+1, total_questions):
        if questions[i] > questions[j]:
            questions[i], questions[j] = questions[j], questions[i]

print("Selected questions in order:", questions)

