# rock-paper-scissors.py
# Main entry point. Runs the menu loop and tracks scores.

from game import Game


def show_scores(scores):
    """Display the current score tally."""
    print("\n  --- Scores ---")
    print(f"  Wins  : {scores['win']}")
    print(f"  Losses: {scores['loss']}")
    print(f"  Draws : {scores['draw']}")
    print("  --------------")


def main():
    game   = Game()
    scores = {"win": 0, "loss": 0, "draw": 0}

    print("\n================================")
    print("    ROCK  PAPER  SCISSORS")
    print("================================")

    while True:
        print("\n  1. Play a new game")
        print("  2. Show scores")
        print("  3. Quit")
        option = input("\n  Choose an option (1/2/3): ").strip()

        if option == "1":
            result = game.play()
            scores[result] += 1

            if result == "win":
                print("  You win!")
            elif result == "loss":
                print("  You lose.")
            else:
                print("  It's a draw!")

        elif option == "2":
            show_scores(scores)

        elif option == "3":
            show_scores(scores)
            print("\n  Thanks for playing! \n")
            break

        else:
            print("  ⚠  Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()