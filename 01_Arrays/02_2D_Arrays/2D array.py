# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - 2D Array Traversals
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Demonstrate initialization, element indexing, row-by-row traversal,
#    and nested loop printing patterns for a 2D matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - 2D Matrix Grid: Represented as a list of lists where arr[row][col] accesses element at row `row` and column `col`.
#    - Nested Loop Traversal: Outer loop handles rows, inner loop handles columns.
#
# 💡 APPROACH:
#    1. Access direct element using grid coordinates arr[row][col].
#    2. Traverse entire matrix by looping row from 0 to rows-1 and col from 0 to cols-1.
#
# 📊 EXAMPLE:
#    Input Matrix:
#    [
#      [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90]
#    ]
#    Output: Row by row printing of elements and pattern.
#
# 🔄 DRY RUN:
#    row = 0: col = 0 (10), col = 1 (20), col = 2 (30)
#    row = 1: col = 0 (40), col = 1 (50), col = 2 (60)
#    row = 2: col = 0 (70), col = 1 (80), col = 2 (90)
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — R rows and C columns traversed.
# 🗂️  SPACE COMPLEXITY: O(1) — No extra space allocated.
#
# 🎯 INTERVIEW POINTS:
#    - Matrix operations require understanding row-major vs column-major order.
#    - In Python, len(arr) gives number of rows, len(arr[0]) gives number of columns.
#
# ⚠️  COMMON MISTAKES:
#    - Indexing cols with row variables or getting IndexError with non-square matrices.
#
# ============================================================

# arr = [
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]

# print(arr)

# for row in range (3):
#     print("Row started: ")
#     for col in range(3):
#         print(arr[row][col], end = " ")
#     print()

# print(arr[0][2])


# for row in range(5):
#     for col in range(2):
#         print("*", end = " ")
#     print()
