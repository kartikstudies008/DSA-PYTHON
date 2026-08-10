# ============================================================
# TOPIC: 01_Arrays / 04_Two_Pointers - Remove Element (LeetCode 27)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an array arr and a value val, remove all instances of val in-place
#    and return the new length / slice of the modified array.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Two Pointers (Slow & Fast): `slow` pointer acts as target boundary for valid elements,
#      `fast` pointer scans array.
#
# 💡 APPROACH:
#    1. Set slow = 0.
#    2. Loop fast from 0 to len(arr)-1.
#    3. If arr[fast] != val: copy arr[fast] into arr[slow] and increment slow.
#    4. Print arr[:slow] representing elements not equal to val.
#
# 📊 EXAMPLE:
#    Input: arr = [3, 2, 2, 3], val = 3
#    Output: [2, 2] (length = 2)
#
# 🔄 DRY RUN:
#    slow = 0
#    fast = 0 (val 3 == 3): skip
#    fast = 1 (val 2 != 3): arr[0] = 2, slow = 1
#    fast = 2 (val 2 != 3): arr[1] = 2, slow = 2
#    fast = 3 (val 3 == 3): skip
#    Result arr[:2] = [2, 2]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Linear scan over array.
# 🗂️  SPACE COMPLEXITY: O(1) — In-place array update.
#
# 🎯 INTERVIEW POINTS:
#    - Return index `slow` represents the new length of valid elements.
#
# ⚠️  COMMON MISTAKES:
#    - Trying to use `arr.remove(val)` inside a loop which results in O(N^2) time complexity.
#
# ============================================================

arr = [3,2,2,3]

val = 3
slow = 0

# Fast pointer scans array; slow pointer writes non-target elements
for fast in range(len(arr)):
    if arr[fast] != val:
        arr[slow] = arr[fast]
        slow += 1

print(arr[:slow])
