import random

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


word_list = ["aardvark", "baboon", "camel"]
choice = random.choice(word_list)

display = []
for show in choice:
  display+= "_"
print(display)

print("choice word is: ",choice)

end_of_game = False
lives = 6

while not end_of_game:
  guess = input("guess a letter: ").lower()
  for position in range(len(choice)):
    letter = choice[position]
    if letter == guess:
      display[position] = letter

  print(display)


  if guess not in choice:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Loss")
  
  if "_" not in display:
    end_of_game = True
    print("You Win")

  print(stages[lives])
