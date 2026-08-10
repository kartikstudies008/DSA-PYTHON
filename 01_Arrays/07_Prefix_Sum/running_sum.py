# ============================================================
# TOPIC: 01_Arrays / 07_Prefix_Sum - Running Sum of 1D Array (LeetCode 1480)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an array nums, return the running sum of nums where
#    runningSum[i] = sum(nums[0]…nums[i]).
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Prefix Sum Pattern: Accumulate running total of array prefix elements.
#
# 💡 APPROACH:
#    1. Initialize total = 0 and empty array arr.
#    2. Loop through each number in nums.
#    3. Accumulate total = total + nums[i].
#    4. Append total to result array arr.
#
# 📊 EXAMPLE:
#    Input: nums = [1, 2, 3, 4]
#    Output: arr = [1, 3, 6, 10]
#
# 🔄 DRY RUN:
#    i = 0 (val 1): total = 0 + 1 = 1 -> arr = [1]
#    i = 1 (val 2): total = 1 + 2 = 3 -> arr = [1, 3]
#    i = 2 (val 3): total = 3 + 3 = 6 -> arr = [1, 3, 6]
#    i = 3 (val 4): total = 6 + 4 = 10 -> arr = [1, 3, 6, 10]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Single linear pass.
# 🗂️  SPACE COMPLEXITY: O(N) — Output array of size N (or O(1) if modified in-place).
#
# 🎯 INTERVIEW POINTS:
#    - Prefix sums allow O(1) range sum queries `sum(L...R) = prefix[R] - prefix[L-1]`.
#
# ⚠️  COMMON MISTAKES:
#    - Recomputing sum from 0 to i on each iteration resulting in O(N^2) performance.
#
# ============================================================

nums = [1,2,3,4]
arr = []
total = 0

# Accumulate running total in single pass
for i in range (len(nums)):
    total = total + nums[i] 
    arr.append(total)

print(arr)
