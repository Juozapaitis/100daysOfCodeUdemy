import random
from art import logo
#Number Guessing Game Objectives:

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Checks answer against guess, returns the number of turns remaining"""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS
  else:
    return "Wrong input"



def game():
  answer = random.randint(1, 101)

  print("Welcome to the number game!")
  print("I'm thinking of a number between 1 and 100")


  print(f"The answer is {answer} ")

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      return print(f"You've run out of guesses, you lose. The answer was {answer}")
    elif guess != answer:
      print("Guess again")


game()