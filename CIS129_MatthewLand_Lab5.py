# Lab 5 - The Bottle Return Program
# Author: Matthew Land
# Date: 10/11/2024
# This program calculates the total number of bottles returned over a week 
# and the total payout for the bottles.

def bottle_return_program():
    # Step 1: Declare variables below 
    total_bottles = 0         # Accumulates the total number of bottles returned
    today_bottles = 0         # Stores the number of bottles returned today
    total_payout = 0          # Stores the total payout
    keep_going = "y"          # Loop control variable initialized to "y"

    # Step 2: Loop to run program again
    while keep_going.lower() == "y":
        # Reset total_bottles for the new week
        total_bottles = 0
        
        # Loop to get the number of bottles returned for 7 days
        for counter in range(1, 8):  
            today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
            total_bottles += today_bottles  

        # Step 3: Calculate total payout
        PAYOUT_PER_BOTTLE = 0.10  
        total_payout = total_bottles * PAYOUT_PER_BOTTLE  
        
        # Print results
        print(f"The total number of bottles collected is: {total_bottles}")
        print(f"The total payout for the week is: ${total_payout:.2f}")

        # Ask the user if they want to enter another week's worth of data
        keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

# Call the function to run the program
bottle_return_program()
print('Thank you for using this program!')
     
    

