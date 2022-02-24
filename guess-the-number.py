import random

logo = """

 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|

"""
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    turns -= 1
    return turns
  elif guess < answer:
    print("To low.")
    turns -= 1
    return turns
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    lives = 10
    return lives
  elif level == "hard":
    lives = 5
    return lives


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking a number between 1 and 100")
  answer = random.randint(1, 100)

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remining to the guess number.")
    guess = int(input("Guess a number: "))

    turns = check_answer(guess, answer, turns)
    
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again!")


game()