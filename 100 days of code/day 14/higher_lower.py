import random
import os
from art import logo, vs
from game_data import data

clear = lambda: os.system('cls')

def choose_person(data):
  accountA = random.choice(data)
  accountB = random.choice(data)
  while accountA == accountB:
    accountB = random.choice(data)

  print(accountA)
  print(accountB)
  # personA = 

def format_data(account):
  account_name = account["name"]
  account_follower_count = account["follower_count"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """Take the ussers guess and follower counts and return if guess is right"""
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"

print(logo)
score = 0
game_should_continue = True
accountB = random.choice(data)

while game_should_continue:

  accountA = accountB
  accountB = random.choice(data)
  while accountA == accountB:
    accountB = random.choice(data)

  print(f"Compare A: {format_data(accountA)}.")
  print(vs)
  print(f"Compare B: {format_data(accountB)}.")

  guess = input("Who do you think has more followers?: 'A' or 'B': ").upper()

  a_follower_count = accountA["follower_count"]
  b_follower_count = accountB["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score += 1
    clear()
    print(f"You're right. Current score = {score} \n")
  else:
    game_should_continue = False
    print(f"You are wrong. The final score is = {score}")
    
    play_again = input("Do you want to play again? 'yes' or 'no' ").lower()
    if play_again == "yes":
      score = 0
      clear()
      game_should_continue = True

  
  # play_again = input("Do you want to play again? 'yes' or 'no' ").lower()
  # if play_again == "yes":
  #   clear()
  #   game_should_continue = True

