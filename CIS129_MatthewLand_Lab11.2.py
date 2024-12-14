try:
    # Open the file to read
    with open("grades.txt", "r") as file:
        grades = [int(line.strip()) for line in file]
      
    # Display grades
    print("Grades:", grades)
      
    # Calculate and display total, count, and average
    count = len(grades)
    total = sum(grades)
    average = total / count if count > 0 else 0
    print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
except FileNotFoundError:
    print("Error: grades.txt file not found. Please ensure the files exists first.")
