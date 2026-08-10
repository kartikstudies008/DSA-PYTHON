# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Search Target in 2D Array
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Search for a target value in a 2D matrix. If present, print its row
#    and column indices.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Brute Force Grid Search: Inspect each cell sequentially until target is found.
#
# 💡 APPROACH:
#    1. Set target value and found flag = False.
#    2. Loop rows and columns using nested loops.
#    3. If target == arr[row][col], print indices, set found = True and break.
#    4. If loop completes and found == False, print "Not Found".
#
# 📊 EXAMPLE:
#    Input: Grid = [[10,20,30],[40,50,60],[70,80,90]], Target = 904
#    Output: NHI MILA HEHEHE
#
# 🔄 DRY RUN:
#    Target = 904. Loops check all 9 cells. No match found. Output failure message.
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — Unsorted 2D array search.
# 🗂️  SPACE COMPLEXITY: O(1) — No additional space used.
#
# 🎯 INTERVIEW POINTS:
#    - Unsorted 2D array requires O(R * C) linear scan.
#    - Binary search O(log(R*C)) can be used if row & col are sorted.
#
# ⚠️  COMMON MISTAKES:
#    - `break` only breaks out of inner loop, outer loop continues unless handled with flag.
#
# ============================================================

arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

# target = 90

# found = False

# for row in range (len(arr)):
#     for col in range(len(arr[row])):

#         if target == arr[row][col]:
#             print("FOUND")

#             print("Row =" , row)
#             print("Col =", col)

#             found = True

#             break

# if found == False:
#         print("NAHI MILA YR ")



target = 904

found = False

for row in range(len(arr)):
    for col in range(len(arr[row])):

        if target == arr[row][col]:
            print("FOUND")

            print("ROW: ",row)
            print("COL: ",col)

            found = True
            break

if found == False:
    print("NHI MILA HEHEHE")
