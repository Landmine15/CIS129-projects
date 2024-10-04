# Module 4 Lab-4
# Matthew Land
# 10/4/2024
# This program calculates and prints the store bonus and individual employee bonuses for 
# The store bonus is based on monthly sales, while individual bonuses are determined by the percent increase in sales.

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Enter the monthly sales amount: "  # prompt will be a string literal

# This code gets the monthly sales
monthlySales = float(input(prompt))

# This code determines the store bonus
if monthlySales > 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input("Enter the percent of sales increase (e.g., 5 for 5%): "))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')
