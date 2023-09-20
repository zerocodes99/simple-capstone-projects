import random
import os
from art import logo, vs
from game_data import data

def get_random_choice():
  """This function returns a random choice from given data list"""
  return random.choice(data)

def get_account_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, {country}"

def check_answer(guess, a_followers, b_followers):
  """This will check the user input & give the appropriate answer to it"""
  if guess == "a":
    if a_followers > b_followers:
      return True
    else:
      return False
  elif guess == "b":
    if b_followers > a_followers:
      return True
    else:
      return False

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_b = get_random_choice()
  
  while game_should_continue:
    account_a = account_b
    account_b = get_random_choice()
    if account_a == account_b:
      account_b = get_random_choice()
  
    print(f"Compare A: {get_account_data(account_a)}")
    print(vs)
    print(f"Against B: {get_account_data(account_b)}")
  
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    os.system('cls')
    print(logo)
  
    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()