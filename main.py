import games.nok as nok
import games.progression as progression
import game_engine


def main():
    print("Select game:")
    print("1 - Least Common Multiple Game")
    print("2 - Progression Game")
    game_choice = input()

    if game_choice == "1":
        game_engine.run_game(nok.game_logic, nok.game_description)
    elif game_choice == "2":
        game_engine.run_game(progression.game_logic, progression.game_description)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()