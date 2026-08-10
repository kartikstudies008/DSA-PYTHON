# ============================================================
# TOPIC: 01_Arrays / 04_Two_Pointers - Move Zeroes (LeetCode 283)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an integer array nums, move all 0's to the end of it while maintaining
#    the relative order of the non-zero elements in-place.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Two Pointers (Slow & Fast):
#      `slow` pointer marks the index where next non-zero element should be written.
#      `fast` pointer scans through the array to discover non-zero elements.
#
# 💡 APPROACH:
#    1. Set slow = 0.
#    2. Iterate fast from 0 to len(arr)-1.
#    3. If arr[fast] != 0, write arr[slow] = arr[fast] and increment slow.
#    4. Once fast finishes, loop slow to len(arr)-1 and set arr[slow] = 0.
#
# 📊 EXAMPLE:
#    Input:  arr = [0, 1, 0, 3, 12]
#    Output: arr = [1, 3, 12, 0, 0]
#
# 🔄 DRY RUN:
#    Initial: arr = [0, 1, 0, 3, 12], slow = 0
#    fast = 0 (val 0): skip
#    fast = 1 (val 1): arr[0] = 1, slow = 1 -> arr = [1, 1, 0, 3, 12]
#    fast = 2 (val 0): skip
#    fast = 3 (val 3): arr[1] = 3, slow = 2 -> arr = [1, 3, 0, 3, 12]
#    fast = 4 (val 12): arr[2] = 12, slow = 3 -> arr = [1, 3, 12, 3, 12]
#    Fill Zeroes from slow=3 to 4: arr[3]=0, arr[4]=0 -> arr = [1, 3, 12, 0, 0]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Linear traversal over array twice (N write steps total).
# 🗂️  SPACE COMPLEXITY: O(1) — Modifies array in-place.
#
# 🎯 INTERVIEW POINTS:
#    - In-place modification constraint avoids creating extra arrays.
#    - Minimizes number of operations compared to swapping on every non-zero.
#
# ⚠️  COMMON MISTAKES:
#    - Forgetting the second loop that fills remaining positions with zeroes.
#
# ============================================================

arr = [0,1,0,3,12]

slow = 0 

# First pass: shift non-zero elements forward
for fast in range(len(arr)):

    if arr[fast] != 0 :
        arr[slow] = arr[fast]
        slow += 1 

# Second pass: fill remaining array with zeroes
while slow < len(arr):
        arr[slow] = 0
        slow += 1

print(arr)
