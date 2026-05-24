# Mini Project 2 : Rock Paper Scissors (OOP + modules pattern)
# Concepts: classes, methods, OOP, separation of concerns

import random



# game_logic.py  (simulated as a class in a real project this would be its
#                 own file and imported with: from game_logic import GameLogic)

class GameLogic:
    """Encapsulates all game rules for Rock Paper Scissors."""

    CHOICES = ["rock", "paper", "scissors"]

    # Maps each choice to what it defeats
    BEATS = {
        "rock":     "scissors",
        "paper":    "rock",
        "scissors": "paper",
    }

    EMOJI = {
        "rock":     "🪨",
        "paper":    "📄",
        "scissors": "✂️ ",
    }

    @staticmethod
    def get_cpu_choice():
        """Return a random choice for the computer."""
        return random.choice(GameLogic.CHOICES)

    @staticmethod
    def get_result(player_choice, cpu_choice):
        """
        Compare choices and return 'win', 'lose', or 'draw'
        from the human player's perspective.
        """
        if player_choice == cpu_choice:
            return "draw"
        if GameLogic.BEATS[player_choice] == cpu_choice:
            return "win"
        return "lose"


# scoreboard.py  (simulated as a class)

class Scoreboard:
    """Tracks and displays the running score across rounds."""

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.history = []

    def record(self, result, player_choice, cpu_choice):
        """Record the outcome of one round."""
        if result == "win":
            self.wins += 1
        elif result == "lose":
            self.losses += 1
        else:
            self.draws += 1
        self.history.append((player_choice, cpu_choice, result))

    def display(self):
        """Print the current scoreboard."""
        total = self.wins + self.losses + self.draws
        print(f"\n  Scoreboard after {total} round(s):")
        print(f"  You: {self.wins}  |  Computer: {self.losses}  |  Draws: {self.draws}")

    def display_history(self):
        """Print a summary of all rounds played."""
        if not self.history:
            print("  No rounds played yet.")
            return
        print("\n  Round history:")
        for i, (p, c, r) in enumerate(self.history, 1):
            ep = GameLogic.EMOJI.get(p, p)
            ec = GameLogic.EMOJI.get(c, c)
            label = {"win": "You won", "lose": "You lost", "draw": "Draw"}[r]
            print(f"   Round {i:>2}: {ep} {p:<8} vs {ec} {c:<8} → {label}")



# game.py  (main entry point : simulated here, would import the above)

class RockPaperScissorsGame:
    """Orchestrates the Rock Paper Scissors game loop."""

    def __init__(self):
        self.logic = GameLogic()
        self.scoreboard = Scoreboard()

    def get_player_choice(self):
        """Prompt the player and return a validated choice."""
        options = "/".join(GameLogic.CHOICES)
        while True:
            raw = input(f"\n  Your move ({options}): ").strip().lower()
            if raw in GameLogic.CHOICES:
                return raw
            # Allow shorthand: r, p, s
            shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
            if raw in shortcuts:
                return shortcuts[raw]
            print(f"  Invalid choice. Enter rock, paper, scissors (or r/p/s).")

    def play_round(self):
        """Play a single round and return whether the user wants to continue."""
        player = self.get_player_choice()
        cpu = self.logic.get_cpu_choice()
        result = self.logic.get_result(player, cpu)

        ep = GameLogic.EMOJI.get(player, player)
        ec = GameLogic.EMOJI.get(cpu, cpu)

        print(f"\n  You chose  : {ep} {player}")
        print(f"  Computer  : {ec} {cpu}")

        if result == "win":
            print(f"  You win! {player.capitalize()} beats {cpu}.")
        elif result == "lose":
            print(f"  You lose. {cpu.capitalize()} beats {player}.")
        else:
            print(f"  It's a draw!")

        self.scoreboard.record(result, player, cpu)
        self.scoreboard.display()

    def run(self):
        """Main game loop."""
        print("\n" + "=" * 35)
        print("     ROCK  PAPER  SCISSORS")
        print("=" * 35)
        print("  Shortcuts: r = rock, p = paper, s = scissors")

        while True:
            self.play_round()
            again = input("\n  Play another round? (y/n): ").strip().lower()
            if again != "y":
                break

        self.scoreboard.display_history()
        print("\n  Thanks for playing! \n")


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()