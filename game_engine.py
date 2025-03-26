def run_game(game_logic, game_description):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)

    for _ in range(3):
        question, correct_answer = game_logic()
        print("Question:", *question)
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")