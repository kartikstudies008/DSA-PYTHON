# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Even and Odd Count in 2D Array
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Count the number of even numbers and odd numbers present in a 2D matrix.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Full Grid Scan: Iterating through every cell of a 2D grid.
#    - Parity Check: Using modulus operator `% 2 == 0` to check evenness.
#
# 💡 APPROACH:
#    1. Initialize counters even = 0, odd = 0.
#    2. Outer loop row through len(arr).
#    3. Inner loop col through len(arr[row]).
#    4. If element % 2 == 0 increment even, else increment odd.
#
# 📊 EXAMPLE:
#    Input Matrix:
#    [ [10, 20, 30],
#      [41, 50, 63],
#      [70, 81, 90] ]
#    Evens: 10, 20, 30, 50, 70, 90 (Count = 6)
#    Odds:  41, 63, 81             (Count = 3)
#
# 🔄 DRY RUN:
#    row 0: 10(E), 20(E), 30(E) -> even=3, odd=0
#    row 1: 41(O), 50(E), 63(O) -> even=4, odd=2
#    row 2: 70(E), 81(O), 90(E) -> even=6, odd=3
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — Must check every element in grid.
# 🗂️  SPACE COMPLEXITY: O(1) — Uses two counters.
#
# 🎯 INTERVIEW POINTS:
#    - Handle non-square matrices by using `len(arr[row])` for inner loop bound.
#
# ⚠️  COMMON MISTAKES:
#    - Hardcoding matrix column limits instead of using len(arr[row]).
#
# ============================================================

arr = [
    [10,20,30],
    [41,50,63],
    [70,81,90]
]

even = 0
odd = 0

# for row in range(len(arr)):
#     for col in range(len(arr[row])):

#         if arr[row][col] % 2 == 0:

#             even = even +1

#         else:

#             odd = odd + 1

# print("EVEN: ",even)
# print("ODD: ",odd)


# Full 2D grid iteration
for row in range (len(arr)):
    for col in range (len(arr[row])):

        if arr[row][col] % 2 == 0:
            even = even + 1
        else: 
            odd = odd + 1

print(even)
print(odd)
