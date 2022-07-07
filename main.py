import random
from replit import clear
from art import logo, vs
from game_data import data

def first_random():
  global first_compare_name
  global first_compare_followers
  global first_compare_description
  global first_compare_country
  first_random = random.randint(0, 50)
  first_compare_name = data[first_random]['name']
  first_compare_followers = data[first_random]['follower_count']
  first_compare_description = data[first_random]['description']
  first_compare_country = data[first_random]['country']
first_random()

def second_random():
  global second_compare_name
  global second_compare_followers
  global second_compare_description
  global second_compare_country
  second_random = random.randint(0, 50)
  second_compare_name = data[second_random]['name']
  second_compare_followers = data[second_random]['follower_count']
  second_compare_description = data[second_random]['description']
  second_compare_country = data[second_random]['country']
second_random()

print(logo)

def game():
  score = 0 
  game_continue = True
  while game_continue == True:
    # print(f"Current Score: {score}")
    print(f"Compare A: {first_compare_name}, {first_compare_description}, {first_compare_country}")
    print(first_compare_followers)
    print(vs)
    print(f" Compare B: {second_compare_name}, {second_compare_description}, {second_compare_country}")
    print(second_compare_followers)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
      if first_compare_followers > second_compare_followers:
        score += 1
        game_continue = True
        clear()
        second_random()
        print(logo)
        game()
      elif second_compare_followers > first_compare_followers:
        game_continue = False
        clear()
        print(logo)
        print(f"Sorry, that is wrong. Final score: {score}")
      else: 
        clear()
        second_random
    elif guess == "b":
      if second_compare_followers > first_compare_followers:
        score += 1
        game_continue = True
        clear()
        first_random()
        print(logo)
        game()
      elif first_compare_followers > second_compare_followers:
        game_continue = False
        clear()
        print(logo)
        print(f"Sorry, that is wrong. Final score: {score}")
      else: 
        clear()
        first_random()
        second_random()
      
game()

    
  