import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
print(logo)

chosen_word = random.choice(word_list)
lives = 6

#Testing code
#print(f"Pssst, tje solutions is {chosen_word}")

display = []

for _ in chosen_word:
  display.append("_")

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for letter in range(len(chosen_word)):
    #print(f"Current position: {letter} \n Current letter {chosen_word[letter]}\n Guessed letter: {guess}")
    if chosen_word[letter] == guess:
      display[letter] += chosen_word[letter]
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win.")
  
  print(stages[lives])