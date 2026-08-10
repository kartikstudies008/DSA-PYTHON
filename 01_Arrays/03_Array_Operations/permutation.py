# ============================================================
# TOPIC: 01_Arrays / 03_Array_Operations - Build Array from Permutation (LeetCode 1920)
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given a zero-based permutation nums, build an array ans of the same length
#    where ans[i] = nums[nums[i]] for each 0 <= i < nums.length.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Indirect Array Indexing: Using element value nums[i] as the target index for lookup.
#
# 💡 APPROACH:
#    1. Create empty array ans.
#    2. Loop i through len(nums).
#    3. Access index idx = nums[i].
#    4. Append nums[idx] to ans.
#
# 📊 EXAMPLE:
#    Input: nums = [0, 2, 1, 5, 3, 4]
#    Output: ans = [0, 1, 2, 4, 5, 3]
#
# 🔄 DRY RUN:
#    i = 0: nums[0] = 0 -> ans.append(nums[0]) -> ans = [0]
#    i = 1: nums[1] = 2 -> ans.append(nums[2]) -> ans = [0, 1]
#    i = 2: nums[2] = 1 -> ans.append(nums[1]) -> ans = [0, 1, 2]
#    i = 3: nums[3] = 5 -> ans.append(nums[5]) -> ans = [0, 1, 2, 4]
#    i = 4: nums[4] = 3 -> ans.append(nums[3]) -> ans = [0, 1, 2, 4, 5]
#    i = 5: nums[5] = 4 -> ans.append(nums[4]) -> ans = [0, 1, 2, 4, 5, 3]
#
# ⏱️  TIME COMPLEXITY:  O(N) — Single loop through nums.
# 🗂️  SPACE COMPLEXITY: O(N) — Extra array of size N for answer.
#
# 🎯 INTERVIEW POINTS:
#    - Can be solved in O(1) extra space using bit manipulation / math encoding `nums[i] = nums[i] + N * (nums[nums[i]] % N)`.
#
# ⚠️  COMMON MISTAKES:
#    - Chaining indices incorrectly or getting confused with indirect access.
#
# ============================================================

nums  = [0,2,1,5,3,4]

ans = []

# Indirect indexing: ans[i] = nums[nums[i]]
for i in range(len(nums)):
    ans.append(nums[nums[i]])

print(ans)
