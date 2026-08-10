# ============================================================
# TOPIC: 01_Arrays / 05_Searching - Linear Search
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Search for a target value in an array by inspecting elements one by one.
#    Print index if found, else state element is not present.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Sequential Search: Checks every element from start to finish. Works on unsorted arrays.
#
# 💡 APPROACH:
#    1. Read array elements and target search value from input.
#    2. Set found = False.
#    3. Loop i from 0 to len(arr)-1:
#       If arr[i] == search, print index i, set found = True and break.
#    4. If not found, print "elem not found".
#
# 📊 EXAMPLE:
#    Input Array: [10, 20, 30], Target: 20
#    Output: elem found at index: 1
#
# 🔄 DRY RUN:
#    i = 0 (val 10): 10 != 20 -> continue
#    i = 1 (val 20): 20 == 20 -> found at index 1! Break loop.
#
# ⏱️  TIME COMPLEXITY:  O(N) — Worst case checks all N elements.
# 🗂️  SPACE COMPLEXITY: O(1) — No extra space used.
#
# 🎯 INTERVIEW POINTS:
#    - Linear Search is O(N) time complexity and requires no sorting.
#    - Binary Search is O(log N) but requires sorted array.
#
# ⚠️  COMMON MISTAKES:
#    - Forgetting `break` after finding element, causing unnecessary checks.
#
# ============================================================

arr = []
size = int(input("enter size: "))

for i in range(size):
    num = int(input("enter elem: "))
    arr.append(num)

print(arr)

search = int(input("enetr elem search: "))

found = False

# Sequential search for target element
for i in range (len(arr)):
    if arr[i] == search:
        print("elem found at index: ",i)
        found = True
        break

if not found :
    print("elem not found yr ")
