# ============================================================
# TOPIC: 01_Arrays / 02_2D_Arrays - Transpose of 2D Matrix
# ============================================================
#
# 📌 PROBLEM STATEMENT:
#    Given a 2D matrix, compute its transpose (flip matrix over its main diagonal,
#    swapping rows and columns).
#
# 🧠 DSA CONCEPT / PATTERN:
#    - Matrix Transposition: Element at original position (row, col) moves to (col, row) in target matrix.
#
# 💡 APPROACH:
#    1. Create empty output matrix `transpose` with dimensions (Cols x Rows).
#    2. Loop row through input matrix rows.
#    3. Loop col through input matrix columns.
#    4. Assign transpose[col][row] = arr[row][col].
#
# 📊 EXAMPLE:
#    Input: 2x3 matrix [[1,2,3],[4,5,6]]
#    Output: 3x2 matrix [[1,4],[2,5],[3,6]]
#
# 🔄 DRY RUN:
#    row 0, col 0: transpose[0][0] = arr[0][0] = 1
#    row 0, col 1: transpose[1][0] = arr[0][1] = 2
#    row 0, col 2: transpose[2][0] = arr[0][2] = 3
#    row 1, col 0: transpose[0][1] = arr[1][0] = 4
#    row 1, col 1: transpose[1][1] = arr[1][1] = 5
#    row 1, col 2: transpose[2][1] = arr[1][2] = 6
#
# ⏱️  TIME COMPLEXITY:  O(R * C) — Copies all elements into transposed grid.
# 🗂️  SPACE COMPLEXITY: O(R * C) — Space for transposed grid result.
#
# 🎯 INTERVIEW POINTS:
#    - For square matrix N x N, transposition can be done in-place by swapping arr[i][j] with arr[j][i] for j > i.
#
# ⚠️  COMMON MISTAKES:
#    - Transposing in-place with non-square matrix causes dimension mismatches.
#
# ============================================================

arr = [
    [1,2,3],
    [4,5,6]
]

transpose = [
    [0,0],
    [0,0],
    [0,0]
]

# Map arr[row][col] into transpose[col][row]
for row in range(len(arr)):
    for col in range(len(arr[row])):
        transpose[col][row] = arr[row][col]

print (transpose)
