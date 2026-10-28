
# Multi-Branch Expense Matrix Analysis

branches = ["Branch A", "Branch B", "Branch C"]
categories = ["Rent", "Salary", "Transport"]

# Each row represents a branch.
# Each column represents an expense category.
expenses = [
    [10000, 25000, 5000],
    [12000, 30000, 8000],
    [8000, 20000, 4000]
]

print("MULTI-BRANCH EXPENSE ANALYSIS")
print("-" * 45)

grand_total = 0
branch_totals = []

# Calculate branch totals and averages
for i in range(len(branches)):
    total = sum(expenses[i])
    average = total / len(categories)

    branch_totals.append(total)
    grand_total += total

    print("\nBranch:", branches[i])
    print("Total Expense: Rs.", total)
    print("Average Expense: Rs.", round(average, 2))

# Calculate category totals
category_totals = []

print("\nCATEGORY-WISE EXPENSES")
for j in range(len(categories)):
    total = sum(expenses[i][j]
                for i in range(len(branches)))

    category_totals.append(total)

    print(categories[j], ": Rs.", total)

# Identify the largest contributors
largest_branch = branch_totals.index(max(branch_totals))
largest_category = category_totals.index(max(category_totals))

print("\n--- FINAL REPORT ---")
print("Grand Total: Rs.", grand_total)
print("Average Expense per Branch: Rs.",
      round(grand_total / len(branches), 2))

print("Highest Spending Branch:",
      branches[largest_branch])
print("Branch Expense: Rs.", branch_totals[largest_branch])

print("Largest Expense Category:",
      categories[largest_category])
print("Category Expense: Rs.",
      category_totals[largest_category])
