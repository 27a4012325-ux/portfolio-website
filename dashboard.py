import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv("data.csv")

# Calculate total income, expense and savings
total_income = df[df["type"] == "Income"]["amount"].sum()
total_expense = df[df["type"] == "Expense"]["amount"].sum()
savings = total_income - total_expense

print("===== PERSONAL FINANCE DASHBOARD =====")
print(f"Total income: {total_income:,} VND")
print(f"Total expense: {total_expense:,} VND")
print(f"Savings: {savings:,} VND")

# Filter expense data
expense_df = df[df["type"] == "Expense"]

# Group expenses by category
category_expense = expense_df.groupby("category")["amount"].sum()

# Chart 1: Expenses by Category
plt.figure(figsize=(8, 5))
category_expense.plot(kind="bar")
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount (VND)")
plt.tight_layout()
plt.show()

# Chart 2: Expense Distribution
plt.figure(figsize=(6, 6))
category_expense.plot(kind="pie", autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Chart 3: Income, Expense and Savings
summary = pd.Series({
    "Income": total_income,
    "Expense": total_expense,
    "Savings": savings
})

plt.figure(figsize=(7, 5))
summary.plot(kind="bar")
plt.title("Income, Expense and Savings")
plt.ylabel("Amount (VND)")
plt.tight_layout()
plt.show() 
