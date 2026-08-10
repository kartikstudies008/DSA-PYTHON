# ============================================================
# TOPIC: 01_Arrays / 04_Two_Pointers - Merge Sorted Array (LeetCode 88)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
#    as one sorted array in-place. nums1 has size m + n, with trailing 0s.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Backward Two Pointers: Fill nums1 starting from the END (index m+n-1)
#      to prevent overwriting unexamined elements in nums1.
#
# 💡 APPROACH:
#    1. Set i = m - 1 (last valid element in nums1).
#    2. Set j = n - 1 (last element in nums2).
#    3. Set k = m + n - 1 (last position in total nums1 array).
#    4. Compare nums1[i] and nums2[j], place larger value at nums1[k], decrement k and pointer.
#    5. If nums2 still has leftover elements (j >= 0), copy them into nums1.
#
# 📊 EXAMPLE:
#    Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3; nums2 = [2, 5, 6], n = 3
#    Output: nums1 = [1, 2, 2, 3, 5, 6]
#
# 🔄 DRY RUN:
#    i=2 (val 3), j=2 (val 6), k=5: 6 > 3 -> nums1[5] = 6, j=1, k=4
#    i=2 (val 3), j=1 (val 5), k=4: 5 > 3 -> nums1[4] = 5, j=0, k=3
#    i=2 (val 3), j=0 (val 2), k=3: 3 > 2 -> nums1[3] = 3, i=1, k=2
#    i=1 (val 2), j=0 (val 2), k=2: 2 >= 2 -> nums1[2] = 2, j=-1, k=1
#    Loop finishes. Result: [1, 2, 2, 3, 5, 6].
#
# ⏱️  TIME COMPLEXITY:  O(M + N) — Each element processed once.
# 🗂️  SPACE COMPLEXITY: O(1) — In-place array modification.
#
# 🎯 INTERVIEW POINTS:
#    - Filling backwards is the key insight to avoid needing O(M) auxiliary memory.
#
# ⚠️  COMMON MISTAKES:
#    - Merging from front (overwrites nums1 elements before they are compared).
#
# ============================================================

nums1 = [1,2,3,0,0,0] # i tracks end of valid elements in nums1
m = 3
nums2 = [2,5,6]       # j tracks elements in nums2
n = 3

i = m - 1
j = len(nums2)-1
k = len(nums1)-1

# Compare elements from back and place larger element at position k
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    else:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

# Copy remaining elements of nums2 if any exist
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(nums1)
