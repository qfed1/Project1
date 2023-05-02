import csv

# Define the file path for the budget data
file_path = "budget.csv"

# Define variables to hold the total income and expenses
total_income = 0
total_expenses = 0

# Read in the budget data from the CSV file
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    for row in reader:
        category, amount = row
        amount = float(amount)
        
        # Add income to the total income
        if category == "Income":
            total_income += amount
        # Add expenses to the total expenses
        else:
            total_expenses += amount

# Calculate the remaining budget
remaining_budget = total_income - total_expenses

# Display a summary of the budget
print("Budget Summary")
print("--------------")
print(f"Total Income: ${total_income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
