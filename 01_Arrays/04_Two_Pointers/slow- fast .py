# ============================================================
# TOPIC: 01_Arrays / 04_Two_Pointers - Remove Duplicates from Sorted Array (LeetCode 26)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given a sorted array arr, remove the duplicates in-place such that each unique
#    element appears only once. Return the number of unique elements.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Slow & Fast Pointers on Sorted Data: `slow` maintains last known unique element position,
#      `fast` searches ahead for new unique value.
#
# 💡 APPROACH:
#    1. Set slow = 0.
#    2. Loop fast from index 1 to len(arr)-1.
#    3. If arr[fast] != arr[slow], increment slow and copy arr[slow] = arr[fast].
#    4. Unique count is `slow + 1`.
#
# 📊 EXAMPLE:
#    Input:  arr = [1, 1, 2, 2, 3]
#    Output: Unique count = 3, Array prefix = [1, 2, 3]
#
# 🔄 DRY RUN:
#    Initial: arr = [1, 1, 2, 2, 3], slow = 0 (val 1)
#    fast = 1 (val 1): arr[1] == arr[0] -> skip
#    fast = 2 (val 2): arr[2] != arr[0] -> slow = 1, arr[1] = 2 -> arr = [1, 2, 2, 2, 3]
#    fast = 3 (val 2): arr[3] == arr[1] -> skip
#    fast = 4 (val 3): arr[4] != arr[1] -> slow = 2, arr[2] = 3 -> arr = [1, 2, 3, 2, 3]
#    Final unique count = slow + 1 = 3.
#
# ⏱️  TIME COMPLEXITY:  O(N) — Single pass over array.
# 🗂️  SPACE COMPLEXITY: O(1) — Modified array in-place.
#
# 🎯 INTERVIEW POINTS:
#    - Works because input array is sorted (identical values are adjacent).
#
# ⚠️  COMMON MISTAKES:
#    - Starting fast from 0 instead of 1, causing redundant self-comparisons.
#
# ============================================================

arr = [1,1,2,2,3]

slow = 0

# Fast pointer scans for new distinct elements
for fast in range(1,len(arr)):

    if arr[fast] != arr[slow]:
        slow += 1 
        arr[slow] = arr[fast]

print(slow + 1) # Print number of unique elements
print(arr[:slow + 1]) # Print slice of unique elements
print(arr) # Print overall array state
