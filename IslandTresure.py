# you need to give three inputs according to conditions
# play and enjoy

print("welcome Island your mission is to find tresure")

choice1 = input("You are in a island which side you want to go 'left' or 'right' : ")

if choice1 == 'right':
  print("game Over")
if choice1 == 'left':
  print("you came to beach")
  choice2 = input("Do you wnat to 'swim' or wite for 'wait' for boat: ") 
  if choice2 == 'swim':
    print("game Over")
  if choice2 == 'wait':
    print("Waiting....")
    choice3 = input("which dore you wnat to opne 'red' 'blue' 'yellow' : ")
    if choice3 == 'red':
      print("game Over")
    elif choice3 == 'blue':
      print("game Over")
    elif choice3 == 'yellow':
      print("***YOU WON***")
