import random

numbers = random.randint(1, 100)
print(numbers)
question_count = 0

question = int(input("Write a random number? "))
question_count = question_count + 1

while question != numbers:
    if question > numbers:
        print("Too high. Try again")
    elif question < numbers:
        print("Too low, Try again")
    question = int(input("Write a random number? "))

print("Correct!")

print (f"You got it in {question_count} tries")