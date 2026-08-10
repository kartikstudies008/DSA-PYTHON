# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Row Sum and Column Sum of 2D Matrix
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Calculate sum of each row and sum of each column independently in a 2D matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Row-Major Traversal: Outer loop row, inner loop col (calculates row sums).
#    - Column-Major Traversal: Outer loop col, inner loop row (calculates column sums).
#
# 💡 APPROACH:
#    1. Column Sums: Loop col from 0 to 2. Reset sum = 0. Loop row from 0 to 2. Add arr[row][col]. Print column sum.
#    2. Row Sums (commented snippet): Loop row first, add arr[row][col].
#
# 📊 EXAMPLE:
#    Input Grid:
#    [ [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90] ]
#    Column 1 sum: 10 + 40 + 70 = 120
#    Column 2 sum: 20 + 50 + 80 = 150
#    Column 3 sum: 30 + 60 + 90 = 180
#
# 🔄 DRY RUN (Column Sums):
#    col = 0: sum = 10 + 40 + 70 = 120
#    col = 1: sum = 20 + 50 + 80 = 150
#    col = 2: sum = 30 + 60 + 90 = 180
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — Every element visited.
# 🗂️  SPACE COMPLEXITY: O(1) — Single sum accumulator.
#
# 🎯 INTERVIEW POINTS:
#    - Swap inner and outer loops to change from row-major to column-major order.
#
# ⚠️  COMMON MISTAKES:
#    - Forgetting to reset accumulator sum = 0 at the start of each row/column iteration.
#
# ============================================================

# ROW ADD 
 
arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]

]

# for row in range (3):
#     sum = 0
#     for col in range(3):
#         sum = sum + arr[row][col]

#     print("ROW" , row +1  , "SUM : " ,sum)



# COL ADD (Column-major iteration)

for col in range(3):
    sum  = 0

    for row in range(3):
        sum = sum + arr[row][col]

    print("COL " , col +1 , "SUM: " ,sum)
