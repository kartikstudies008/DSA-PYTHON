# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Both Diagonals Sum
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Calculate the sum of elements on both the primary (main) diagonal
#    and secondary (anti) diagonal of a square matrix. Avoid double-counting
#    the center element for odd-dimension matrices.
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Main Diagonal Indexing: Primary diagonal elements are at arr[i][i].
#    - Anti Diagonal Indexing: Secondary diagonal elements are at arr[i][N - 1 - i].
#    - Matrix Inclusion-Exclusion: Deduct center element arr[N//2][N//2] if N is odd.
#
# 💡 APPROACH:
#    1. Single loop i from 0 to N-1: add arr[i][i] to total sum.
#    2. Single loop i from 0 to N-1: add arr[i][N - 1 - i] to total sum.
#    3. Check if len(arr) is odd. If true, subtract arr[N//2][N//2] once.
#
# 📊 EXAMPLE:
#    Input:
#    [ [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90] ]
#    Main Diag: 10 + 50 + 90 = 150
#    Anti Diag: 30 + 50 + 70 = 150
#    Total without fix = 300, Center element (50) is counted twice.
#    Final Total = 300 - 50 = 250.
#
# 🔄 DRY RUN:
#    Main diag sum: 10 + 50 + 90 = 150
#    Anti diag sum: 30 + 50 + 70 = 150 (Total = 300)
#    Matrix size N = 3 (odd) -> Subtract arr[1][1] (50) -> Total = 250.
#
# ⏱️  TIME COMPLEXITY:  O(N) — Single loop through diagonal elements (N = matrix size).
# 🗂️  SPACE COMPLEXITY: O(1) — Uses single scalar variable total.
#
# 🎯 INTERVIEW POINTS:
#    - Using O(N) single loop per diagonal is optimal compared to O(N^2) full matrix search.
#    - Remember edge case: odd vs even size matrix center intersection.
#
# ⚠️  COMMON MISTAKES:
#    - Forgetting to subtract the center element when matrix size N is odd.
#
# ============================================================

arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

total = 0

# Main diagonal elements: arr[i][i]
for i in range(len(arr)):
    total += arr[i][i]

# Anti diagonal elements: arr[i][N-1-i]
for i in range (len(arr)):
    total += arr[i][len(arr)-1-i]

# If N is odd, subtract center element which was added twice
if len(arr) % 2 == 1:
    total -= arr[len(arr)//2][len(arr)//2]

print(total)
