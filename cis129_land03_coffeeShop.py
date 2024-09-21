#This program is a an interactive text based Coffee Shop simulator that calculates a reciept based on how many items the user wants to order
print('Welcome to Matthew's Coffee Shop!')
print('Here is our menu with prices:')
print('Coffee-------- $5')
print('Muffin-------- $4')
print('Scone-------- $3')
print('Brownie-------- $2')
print('A standard 6% sales tax rate will be added to your subtotal')
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
print('My Coffee and Muffin Shop Receipt')
print(f'{numCoffees} Coffee at $5 each: $ {coffeeTotal:5.2f}')
print(f'{numMuffins} Muffins at $4 each: $ {muffinTotal:5.2f}')
print(f'{numScones} Scones at $3 each: $ {sconeTotal:5.2f}')
print(f'{numBrownies} Brownies at $2 each: $ {brownieTotal:5.2f}')
print(f'6% tax:              $ {tax:5.2f}')
print('---------')
print(f'Total:               $ {total:5.2f}')
print('***************************************')
print('Thank you for coming to My Coffee and Muffin Shop!')
