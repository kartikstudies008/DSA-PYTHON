# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Main Diagonal Sum
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Calculate the sum of all elements along the main (primary) diagonal
#    of a square matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Direct Diagonal Access: On the main diagonal, row index equals column index (row == col == i).
#
# 💡 APPROACH:
#    1. Initialize sum = 0.
#    2. Iterate i from 0 to len(arr)-1.
#    3. Accumulate arr[i][i] into sum.
#
# 📊 EXAMPLE:
#    Input:
#    [ [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90] ]
#    Output: Sum = 10 + 50 + 90 = 150
#
# 🔄 DRY RUN:
#    i = 0: sum = 0 + arr[0][0] = 10
#    i = 1: sum = 10 + arr[1][1] = 10 + 50 = 60
#    i = 2: sum = 60 + arr[2][2] = 60 + 90 = 150
#
# ⏱️  TIME COMPLEXITY:  O(N) — Only N elements visited for N x N matrix.
# 🗂️  SPACE COMPLEXITY: O(1) — Constant space used.
#
# 🎯 INTERVIEW POINTS:
#    - O(N) diagonal access is preferred over O(N^2) double loop checking `if row == col`.
#
# ⚠️  COMMON MISTAKES:
#    - Using nested loops O(N^2) when single loop O(N) is sufficient.
#
# ============================================================

arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

sum = 0

# Access diagonal element arr[i][i] directly
for i in range(len(arr)):
    sum = sum + arr[i][i]

print("The sum of the diagonal elements is:", sum)
