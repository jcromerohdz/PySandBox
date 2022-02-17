import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choose =2 #random.randint(0, 2)

if player_choose == 0 and computer_choose == 0:
    print(f"You choose: \n {rock}")
    print(f"Coputer choose: \n {rock}")
    print("It's a draw!!")
elif player_choose == 1 and computer_choose == 1:
    print(f"You choose: \n {paper}")
    print(f"Coputer choose: \n {paper}")
    print("It's a draw!!")
elif player_choose == 2 and computer_choose == 2:
    print(f"You choose: \n {scissors}")
    print(f"Coputer choose: \n {scissors}")
    print("It's a draw!!")
elif player_choose == 0 and computer_choose == 2:
    print(f"You choose: \n {rock}")
    print(f"Coputer choose: \n {scissors}")
    print("You Win!!")
elif player_choose == 1 and computer_choose == 0:
    print(f"You choose: \n {paper}")
    print(f"Coputer choose: \n {rock}")
    print("You Win!!")
elif player_choose == 2 and computer_choose == 1:
    print(f"You choose: \n {scissors}")
    print(f"Coputer choose: \n {paper}")
    print("You Win!!")
elif player_choose == 2 and computer_choose == 0:
    print(f"You choose: \n {scissors}")
    print(f"Coputer choose: \n {rock}")
    print("You lose!!")
elif player_choose == 0 and computer_choose == 1:
    print(f"You choose: \n {rock}")
    print(f"Coputer choose: \n {paper}")
    print("You lose!!")
elif player_choose == 1 and computer_choose == 2:
    print(f"You choose: \n {paper}")
    print(f"Coputer choose: \n {scissors}")
    print("You lose!!")