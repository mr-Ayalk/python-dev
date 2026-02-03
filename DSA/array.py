# Create the initial list of expenses
# Index: 0 (Jan), 1 (Feb), 2 (Mar), 3 (Apr), 4 (May)
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compared to January?
extra_feb = expenses[1] - expenses[0]
print(f"Extra spent in February: ${extra_feb}")

# 2. Total expense in first quarter (first three months)
total_q1 = expenses[0] + expenses[1] + expenses[2]
# Alternatively: total_q1 = sum(expenses[:3])
print(f"Total Q1 expense: ${total_q1}")

# 3. Find out if you spent exactly 2000 dollars in any month
spent_2000 = 2000 in expenses
print(f"Spent exactly $2000 in any month? {spent_2000}")

# 4. June month just finished (1980 dollars). Add this to the list.
expenses.append(1980)
print(f"Expenses after adding June: {expenses}")

# 5. Returned an item in April, got a $200 refund. Update the list.
# April is index 3.
expenses[3] = expenses[3] - 200
print(f"Expenses after April refund: {expenses}")