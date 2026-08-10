# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Secondary (Anti) Diagonal Sum
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Calculate the sum of elements along the secondary (anti) diagonal of a square matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Anti-Diagonal Property: For row index `i`, column index is `N - 1 - i`.
#
# 💡 APPROACH:
#    1. Set sum = 0.
#    2. Loop i from 0 to N-1.
#    3. Add arr[i][len(arr) - 1 - i] to sum.
#
# 📊 EXAMPLE:
#    Input:
#    [ [10, 20, 30],
#      [40, 50, 60],
#      [71, 80, 90] ]
#    Anti-Diagonal elements: arr[0][2]=30, arr[1][1]=50, arr[2][0]=71.
#    Output: Sum = 30 + 50 + 71 = 151.
#
# 🔄 DRY RUN:
#    i = 0: col = 3-1-0 = 2 -> sum = 0 + 30 = 30
#    i = 1: col = 3-1-1 = 1 -> sum = 30 + 50 = 80
#    i = 2: col = 3-1-2 = 0 -> sum = 80 + 71 = 151
#
# ⏱️  TIME COMPLEXITY:  O(N) — Single loop through N elements.
# 🗂️  SPACE COMPLEXITY: O(1) — Single scalar variable.
#
# 🎯 INTERVIEW POINTS:
#    - Formula for anti-diagonal cell: row + col == N - 1.
#
# ⚠️  COMMON MISTAKES:
#    - Using nested loops O(N^2) instead of a single formula-driven O(N) loop.
#
# ============================================================

arr = [
    [10,20,30],
    [40,50,60],
    [71,80,90]
]

sum = 0

# Access anti-diagonal element directly via index formula
for i in range (len(arr)):
    sum = sum + arr[i][len(arr) - 1 - i]

print("The sum of the diagonal elements is:", sum)
