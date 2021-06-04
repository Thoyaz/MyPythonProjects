Grocery_q = {}
Grocery_p = {}
amount = []


def budget():
	Budget = int(input("enter budget: "))
	amount.append(Budget)


def UserChoice():

	print("1.Add an item \n2.Exit")
	global choice
	choice = int(input("Enter your choice :"))
	if choice == 1:

		product = input("Enter product : ")

		quantity = input("Enter quantity :")

		price = int(input("Enter Price : "))
		global Amount_left
		Amount_left = min(amount) - price
		amount.append(Amount_left)
		print(f"Amount left : {Amount_left}")
		Grocery_q[product] = quantity
		Grocery_p[product] = price


budget()

run = True
while run:
	UserChoice()
	if choice == 2:
		print("EXIT SUCCESFULLY")
		run = False
