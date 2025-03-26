import random

def generate_progression():
    b1 = random.randint(1, 10)
    q = random.randint(2, 5)
    n = random.randint(5, 10)
    progression = [b1 * (q ** i) for i in range(n)]
    hidden_index = random.randint(0, n - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer

def game_logic():
    return generate_progression()

game_description = "What number is missing in the progression?"