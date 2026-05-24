# Contains the Game class with all game logic for Rock Paper Scissors.

import random


class Game:
    """Handles a single round of Rock Paper Scissors."""

    CHOICES = ["rock", "paper", "scissors"]

    BEATS = {
        "rock":     "scissors",
        "paper":    "rock",
        "scissors": "paper",
    }

    def get_user_item(self):
        """Prompt the user and return a valid choice."""
        while True:
            choice = input("  Your move (rock / paper / scissors): ").strip().lower()
            if choice in self.CHOICES:
                return choice
            print("  ⚠  Invalid input. Please enter rock, paper, or scissors.")

    def get_computer_item(self):
        """Return a random choice for the computer."""
        return random.choice(self.CHOICES)

    def get_game_result(self, user_item, computer_item):
        """
        Compare the two choices and return the result
        from the user's perspective: 'win', 'loss', or 'draw'.
        """
        if user_item == computer_item:
            return "draw"
        if self.BEATS[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        """
        Run one round: get both choices, print them, determine the result.
        Returns the result string: 'win', 'loss', or 'draw'.
        """
        user_item     = self.get_user_item()
        computer_item = self.get_computer_item()

        print(f"\n  You chose    : {user_item}")
        print(f"  Computer chose: {computer_item}")

        result = self.get_game_result(user_item, computer_item)
        return result