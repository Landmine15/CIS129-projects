#This program is a an interactive text based Coffee Shop simulator that calculates a reciept based on how many items the user wants to order

#menu prices below
coffeePrice = 5
muffinPrice = 4
taxRate = 0.06

# User input code below
numCoffees = int(input("How many coffees would you like?: "))
numMuffins = int(input("How many muffins would you like?: "))

# Calculating subtotal
coffeeTotal = numCoffees * coffeePrice
muffinTotal = numMuffins * muffinPrice
subtotal = coffeeTotal + muffinTotal


# Calculating tax code below
tax = subtotal * taxRate

# Calculating total code below
total = subtotal + tax

# Output the final results below
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{numCoffees} Coffee at $5 each: $ {coffee_total:5.2f}")
print(f"{num_muffins} Muffins at $4 each: $ {muffin_total:5.2f}")
print(f"6% tax:              $ {tax:5.2f}")
print("---------")
print(f"Total:               $ {total:5.2f}")
print("***************************************")
print(
