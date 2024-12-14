import csv
# Open the file for writing
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    print("Please enter student information. Type 'done' as the first name to end.")
    # Write the header
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    while True:
        firstname = input("Enter first name: ")
        if firstname.lower() == 'done':
            break
        lastname = input("Enter last name: ")
        try:
            exam1 = int(input("Enter grade from exam 1: "))
            exam2 = int(input("Enter grade from exam 2: "))
            exam3 = int(input("Enter grade from exam 3: "))
            # Write student record
            writer.writerow([firstname, lastname, exam1, exam2, exam3])
        except ValueError:
            print("Invalid input for grades. Please enter integers.")
