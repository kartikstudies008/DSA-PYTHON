# ============================================================
# TOPIC: 01_Arrays / 08_LeetCode - Richest Customer Wealth (LeetCode 1672)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an m x n 2D grid accounts where accounts[i][j] is the money of the i-th customer
#    in the j-th bank, return the wealth of the richest customer (maximum row sum).
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Grid Row Sum Accumulation: Find row with maximum sum across 2D matrix.
#
# 💡 APPROACH:
#    1. Set maxWealth = 0.
#    2. Outer loop row through customers.
#    3. Reset sum = 0 for current customer.
#    4. Inner loop col through banks: sum += accounts[row][col].
#    5. Update maxWealth = max(maxWealth, sum).
#
# 📊 EXAMPLE:
#    Input Grid:
#    [ [1, 2, 3],  -> Sum = 6
#      [3, 2, 1],  -> Sum = 6
#      [4, 5, 6] ] -> Sum = 15
#    Output: maxWealth = 15
#
# 🔄 DRY RUN:
#    row 0: sum = 1 + 2 + 3 = 6 -> maxWealth = 6
#    row 1: sum = 3 + 2 + 1 = 6 -> maxWealth = max(6, 6) = 6
#    row 2: sum = 4 + 5 + 6 = 15 -> maxWealth = max(6, 15) = 15
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — R customers, C banks.
# 🗂️  SPACE COMPLEXITY: O(1) — Memory for scalar maxWealth and sum.
#
# 🎯 INTERVIEW POINTS:
#    - Python shortcut: `max(sum(customer) for customer in accounts)`.
#
# ⚠️  COMMON MISTAKES:
#    - Resetting sum outside the outer loop instead of inside per customer row.
#
# ============================================================

arr = [
    [1,2,3],
    [3,2,1],
    [4,5,6]
    ]

maxWealth = 0

# Calculate row sum for each customer
for row in range (3):
    sum = 0 

    for col in range(3):
        sum = sum + arr[row][col]

    if sum > maxWealth :
        maxWealth = sum 

print(maxWealth)
