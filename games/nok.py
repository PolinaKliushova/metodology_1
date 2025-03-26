import math
import random

def find_lcm(numbers):
    return math.lcm(*numbers)

def game_logic():
    numbers = random.sample(range(1, 101), 3)
    return numbers, find_lcm(numbers)

game_description = "Find the smallest common multiple of given numbers."