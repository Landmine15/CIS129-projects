# Open file
with open("grades.txt", "w") as file:
      print("Enter grades, each one by one. Type 'done' to end.")
      while True:
          grade = input("Enter a grade: ")
          if grade.lower() == 'done':
              break
          if grade.isdigit():  # Validate input as a number
              file.write(f"{grade}\n")
          else:
              print("Invalid input. Please enter a number or 'done'.")
print("Grades have been written in grades.txt.")
