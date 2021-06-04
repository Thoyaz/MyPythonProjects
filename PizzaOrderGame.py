# give inputs like
# example: 
#     l
#     y
#     y

# ouputPut = 

# PizzaOrder
# what is the size of the pizza:
# 's' small
# 'L' Large
# 'M' Medium
# do you want pepper: 'y' yes 'n' no: do you want extra chese: 'y' yes 'n' no: Total Bill $ 2


print("PizzaOrder")

small_pizza = 15
Large_Pizza = 20
Medium_Pizza = 25
s_pizza_pepper = 2
L_and_m_pizza_pepper = 3
chese = 1
size = input("what is the size of the pizza: \n 's' small \n 'L' Large \n 'M' Medium \n ")

add_peppor = input("do you want pepper: 'y' yes 'n' no: ")

extra_chese = input("do you want extra chese: 'y' yes  'n' no: ")
# -------------------------------------
def small():
  if size == 's':
      if add_peppor == 'y':
        if extra_chese == 'y':
          bill = small_pizza + s_pizza_pepper + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = small_pizza + s_pizza_pepper
          print("Total Bill $",bill)
        else:
          print("chose correct option: ")
      elif add_peppor == 'n':
        if extra_chese == 'y':
          bill = small_pizza + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = small_pizza 
          print("Total Bill $",bill)
      else:
        print("chose correct option: ")
  else:
    print("chose correct option:")

# ------------------------------------
def Large():
  if size == 'l':
      if add_peppor == 'y':
        if extra_chese == 'y':
          bill = Large_Pizza + L_and_m_pizza_pepper + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = Large_Pizza + L_and_m_pizza_pepper
          print("Total Bill $",bill)
        else:
          print("chose correct option: ")
      elif add_peppor == 'n':
        if extra_chese == 'y':
          bill = Large_Pizza + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = Large_Pizza 
          print("Total Bill $",bill)
      else:
        print("chose correct option: ")
# ---------------------------------------
def Medium():
  if size == 'm':
      if add_peppor == 'y':
        if extra_chese == 'y':
          bill = Medium_Pizza + L_and_m_pizza_pepper + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = Medium_Pizza + L_and_m_pizza_pepper
          print("Total Bill $",bill)
        else:
          print("chose correct option: ")
      elif add_peppor == 'n':
        if extra_chese == 'y':
          bill = Medium_Pizza + chese
          print("Total Bill $",bill)
        elif extra_chese == 'n':
          bill = Medium_Pizza 
          print("Total Bill $",bill)
      else:
        print("chose correct option: ")
  else:
    print("chose correct option:")

if size == 's':
  small()
elif size == 'l':
  Large()
elif size == 'm':
  Medium()
else:
  print("---chose correct option---")
