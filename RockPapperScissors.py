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
chOice = int(input("What do you choose? \n type 0 for Rock \n type 1 for Papper \n type 2 for Scissors\n --> "))

rand = random.randint(0,2)

EmojiList = [rock,paper,scissors]

print("Your Choice: ")

print(EmojiList[chOice])



print("Computer Choice: ")

print(EmojiList[rand])

if EmojiList[chOice] == EmojiList[rand]:
  print("You win")
elif EmojiList[chOice] == EmojiList[rand]:
  print("You Win")
elif EmojiList[chOice] == EmojiList[rand]:
  print("You Win")
else:
  print('You Loss')
