import random
import os
from art import logo

clear = lambda: os.system('cls')

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  # for card in cards:
  #   if sum(cards) > 21 and card == 11:
  #     card = 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "Lose, the opponent has a blackjack"
  elif user_score == 0:
    return "Win, You have a blackjack"
  elif user_score > 21:
    return "Lose, You have more than 21"
  elif computer_score > 21:
    return "Win, computer busted"
  elif user_score > computer_score:
    return "You Win"
  else:
    return f"Lose"

def play_game():

  user_cards = []
  computer_cards = []
  isGameOver = False

  print(logo)

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not isGameOver:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      isGameOver = True
    else:
      getAnother = input("Would you like to get another card? 'yes' or 'no': ")
      if getAnother == "yes":
        user_cards.append(deal_card())
      else:
        isGameOver = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"User cards: {user_cards}, user score: {user_score}")
  print(f"Computer cards: {computer_cards}, computer score: {computer_score}")

  print(compare(user_score, computer_score))

while input("Would you like to play a game of blackjack? 'yes or 'no': ") == 'yes':
  clear()
  play_game()
