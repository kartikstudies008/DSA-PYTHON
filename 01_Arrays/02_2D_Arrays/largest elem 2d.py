# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Find Largest Element in 2D Matrix
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Find the maximum value stored inside a 2D matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Grid Search & Tracking: Initialize max tracker with first cell arr[0][0], update when a larger element is found.
#
# 💡 APPROACH:
#    1. Set l = arr[0][0].
#    2. Iterate through all rows and columns.
#    3. If arr[row][col] > l, set l = arr[row][col].
#
# 📊 EXAMPLE:
#    Input:
#    [ [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90] ]
#    Output: Largest element = 90
#
# 🔄 DRY RUN:
#    l starts at 10.
#    Compare with all values: 20, 30, 40, 50, 60, 70, 80, 90.
#    Max is continuously updated until l = 90.
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — Visited all elements once.
# 🗂️  SPACE COMPLEXITY: O(1) — Extra variable l.
#
# 🎯 INTERVIEW POINTS:
#    - Always initialize max variable with arr[0][0] (or float('-inf')) instead of 0 to handle negative matrices.
#
# ⚠️  COMMON MISTAKES:
#    - Initializing max variable to 0 when matrix might contain negative numbers.
#
# ============================================================

arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

# Initialize with the first element in matrix
l = arr[0][0]

for row in range(len(arr)):
    for col in range(len(arr[row])):

        if arr[row][col] > l:
            l = arr[row][col]

print(l)
