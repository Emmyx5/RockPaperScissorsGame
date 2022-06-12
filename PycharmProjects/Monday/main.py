# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
# This script computes the Rock, Paper, Scissors game

import random
import sys

def ContinueAgain():
       option = input("Do You Want to Continue (Y/N):\n")
       if (option.lower() == "y" or option.lower() == "yes"):
              PerformAction()
       else:
              sys.exit()

def PerformAction():
       games_actions = ["R", "P", "S"]
       player_action = input("Enter a Choice R, P, S:\n")
       if (player_action.__eq__('R') or player_action.__eq__('P')  or player_action.__eq__('S') ):
              computer_action = random.choice(games_actions)
              print(f"\nYou selected {player_action}, computer selected {computer_action}.\n")

              if player_action == computer_action:
                     print(f"Both players selected {player_action}. It's a tie!")
              elif player_action == "R":
                     if computer_action == "S":
                            print("Rock smashes scissors! You win")
                     else:
                            print("Paper covers rock! You lose.")
              elif player_action == "P":
                     if computer_action == "R":
                            print("Paper covers rock! You win!")
                     else:
                            print("Scissors cuts paper!You lose.")
              elif player_action == "S":
                     if computer_action == "P":
                            print("Scissors cuts paper! You win!")
                     else:
                            print("Rock smashes scissors! You lose.")
              ContinueAgain()
       else:
              print("Wrong Input")
              ContinueAgain()

PerformAction()
