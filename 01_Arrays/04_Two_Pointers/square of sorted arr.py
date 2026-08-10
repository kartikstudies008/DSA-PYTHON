# ============================================================
# TOPIC: 01_Arrays / 04_Two_Pointers - Squares of a Sorted Array (LeetCode 977)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given an integer array nums sorted in non-decreasing order, return an array of
#    the squares of each number sorted in non-decreasing order.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Opposite Two Pointers (Left & Right): In a sorted array with negative numbers,
#      largest squared values must come from either extreme left (large negative) or extreme right (large positive).
#
# 💡 APPROACH:
#    1. Set left = 0, right = len(nums) - 1.
#    2. Allocate answer array of size len(nums) and position = len(nums) - 1.
#    3. While left <= right: compare abs(nums[left]) with abs(nums[right]).
#    4. Place square of larger absolute value into answer[position], decrement position, shift corresponding pointer.
#
# 📊 EXAMPLE:
#    Input: nums = [-7, -3, 2, 3, 11]
#    Output: answer = [4, 9, 9, 49, 121]
#
# 🔄 DRY RUN:
#    left=0 (-7), right=4 (11): abs(11) > abs(-7) -> answer[4] = 121, right=3
#    left=0 (-7), right=3 (3): abs(-7) > abs(3) -> answer[3] = 49, left=1
#    left=1 (-3), right=3 (3): abs(-3) == abs(3) -> answer[2] = 9, right=2
#    left=1 (-3), right=2 (2): abs(-3) > abs(2) -> answer[1] = 9, left=2
#    left=2 (2), right=2 (2): answer[0] = 4, left=3
#    Result: [4, 9, 9, 49, 121]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Linear scan filling output array.
# 🗂️  SPACE COMPLEXITY: O(N) — Memory allocated for answer array.
#
# 🎯 INTERVIEW POINTS:
#    - Avoid squaring and sorting O(N log N) by taking advantage of pre-sorted input property with two pointers O(N).
#
# ⚠️  COMMON MISTAKES:
#    - Filling answer array from index 0 instead of filling from back (position = N-1).
#
# ============================================================

nums = [-7,-3,2,3,11]
left = 0
right = len(nums)-1

position = len(nums)-1
answer = [0] * len(nums)

# Fill answer array from largest (back) to smallest (front)
while left <= right:

    if abs(nums[left]) > abs(nums[right]):
        answer[position] = nums[left] ** 2
        left += 1
        position -= 1
    else:
        answer[position] = nums[right] ** 2
        right -= 1
        position -= 1

print(answer)
