

# Budget Tracker

The budget tracker is a simple finance project that allows you to create a budget for the upcoming month. In this project, you will learn how to create a budget using a CSV file and Python script.

## Overview

The budget tracker project involves three main steps:

1. Create a budget in CSV format
2. Write a Python script to read in the budget data and calculate the total income and expenses
3. Display a summary of the budget

## Step 1: Create a budget in CSV format

The first step in creating a budget tracker is to create a budget in CSV format. A CSV file is a simple and easy-to-read format that allows you to store data in rows and columns.

For this project, the budget should include the following categories:

- Income
- Rent
- Utilities
- Groceries
- Transportation
- Entertainment
- Miscellaneous

Each category should have an associated dollar amount. Here's an example budget in CSV format:

```
Category, Amount
Income, 4000
Rent, 1000
Utilities, 200
Groceries, 500
Transportation, 150
Entertainment, 200
Miscellaneous, 150
```

This budget assumes a monthly income of $4,000 and includes typical monthly expenses such as rent, utilities, groceries, transportation, entertainment, and miscellaneous expenses.

## Step 2: Write a Python script to read in the budget data and calculate the total income and expenses

The second step in creating a budget tracker is to write a Python script to read in the budget data and calculate the total income and expenses.

To do this, you can use the `csv` module in Python to read in the budget data from the CSV file. Here's an example Python script that reads in the budget data and calculates the total income and expenses:

```python
import csv

# Define the file path for the budget data
file_path = "budget.csv"

# Define variables to hold the total income and expenses
total_income = 0
total_expenses = 0

# Read in the budget data from the CSV file
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
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
```

This script reads in the budget data from the CSV file, and uses a `for` loop to iterate through each row in the file. For each row, it extracts the category and amount, converts the amount to a float, and adds it to either the total income or total expenses, depending on the category.

Finally, the script calculates the remaining budget by subtracting the total expenses from the total income.

## Step 3: Display a summary of the budget

The final step in creating a budget tracker is to display a summary of the budget.

To do this, you can use the `print` function in Python to display the total income, total expenses, and remaining budget. Here's an example Python script that displays a summary of the budget:

```python
# Display a summary of the budget
print("Budget Summary")
print("--------------")
print(f"Total Income: ${total_income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
```

This script uses the `print` function to display# Project1
