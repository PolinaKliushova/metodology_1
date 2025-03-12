import random
import math

def find_lcm(numbers):
    return math.lcm(*numbers)

def nok_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    while True:
        numbers = random.sample(range(1, 101), 3)
        correct_answer = find_lcm(numbers)
        print("Question: ", *numbers)
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")

def generate_progression():
    b1 = random.randint(1, 10)
    q = random.randint(2, 5)
    n = random.randint(5, 10)
    progression = [b1 * (q ** i) for i in range(n)]
    hidden_index = random.randint(0, n - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer

def progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    while True:
        progression, correct_answer = generate_progression()
        print("Question: ", *progression)
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")




