#README
#This Python program is a simulation that spits out a reciept for an order at "Matthew's Coffee Shop".
#The user is asked to input the number of each item they want to buy.
#The program then calculates the subtotal, applies a 6% tax, and gives a receipt.

#Program:
#- Inputs: Number of coffees, muffins, scones, and brownies.
#- Prices: Coffee is $5 each, Muffins are $4 each, scones are $3 each, and brownies are $2 each
#- Output: A receipt showing the number of items, price breakdown, tax, and total.

#How to Use:
#1. Run the program.
#2. Enter the number of each item when prompted.
#3. The program will display a receipt with itemized prices, tax, and the final total.

print("Welcome to Matthew's Coffee Shop! ")
print('Here is our menu with prices: ')
print('Coffee-------- $5 ')
print('Muffin-------- $4 ')
print('Scone-------- $3 ')
print('Brownie-------- $2 ')
print('A standard 6% sales tax rate will be added to your subtotal ')
#menu prices below
coffeePrice = 5
muffinPrice = 4
sconePrice = 3
browniePrice = 2
taxRate = 0.06

# User input code below
numCoffees = int(input('How many coffees would you like?: '))
numMuffins = int(input('How many muffins would you like?: '))
numScones = int(input('How many scones would you like?: '))
numBrownies = int(input('How many brownies would you like?: '))


# Calculating subtotal
coffeeTotal = numCoffees * coffeePrice
muffinTotal = numMuffins * muffinPrice
sconeTotal = numScones * sconePrice
brownieTotal = numBrownies * browniePrice
subtotal = coffeeTotal + muffinTotal + sconeTotal + brownieTotal


# Calculating tax code below
tax = subtotal * taxRate

# Calculating total code below
total = subtotal + tax

# Output reciept below
print('***************************************')
print("My Matthew's Coffee Shop Receipt")
print(f'{numCoffees} Coffee at $5 each: $ {coffeeTotal:5.2f}')
print(f'{numMuffins} Muffins at $4 each: $ {muffinTotal:5.2f}')
print(f'{numScones} Scones at $3 each: $ {sconeTotal:5.2f}')
print(f'{numBrownies} Brownies at $2 each: $ {brownieTotal:5.2f}')
print(f'6% tax:              $ {tax:5.2f}')
print('---------')
print(f'Total:               $ {total:5.2f}')
print('***************************************')
print("Thank you for coming to Matthew's Coffee Shop!")
