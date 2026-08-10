# ============================================================
# TOPIC: 01_Arrays / 03_Array_Operations - Concatenation of Array (LeetCode 1929)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an integer array nums of length n, create an array ans of length 2n
#    where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Array Appending / Reconstruction: Duplicating elements in sequence.
#
# 💡 APPROACH:
#    1. Initialize empty list arr.
#    2. First loop: Append all elements of nums to arr.
#    3. Second loop: Append all elements of nums to arr again.
#
# 📊 EXAMPLE:
#    Input: nums = [1, 2, 1]
#    Output: arr = [1, 2, 1, 1, 2, 1]
#
# 🔄 DRY RUN:
#    Loop 1: arr becomes [1, 2, 1]
#    Loop 2: arr becomes [1, 2, 1, 1, 2, 1]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Traversing nums twice.
# 🗂️  SPACE COMPLEXITY: O(N) — Auxiliary array of size 2N.
#
# 🎯 INTERVIEW POINTS:
#    - Python shortcut: `nums + nums` or `nums * 2` achieves the exact same result in C-optimized memory blocks.
#
# ⚠️  COMMON MISTAKES:
#    - Indexing errors if allocating fixed-size array without correct size 2*N.
#
# ============================================================

nums = [1,2,1]

arr = []

# First pass: append elements of nums
for i in range(len(nums)):
    arr.append(nums[i])

# Second pass: append elements of nums again
for i in range(len(nums)):
    arr.append(nums[i])

print(arr)
