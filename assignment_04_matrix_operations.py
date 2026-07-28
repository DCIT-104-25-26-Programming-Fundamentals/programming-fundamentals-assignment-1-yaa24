# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Helper function to print a matrix in a neat, aligned grid format."""
    for row in matrix:
        
        print(" ".join(f"{num:4}" for num in row))


def read_matrix(rows, cols, matrix_name="Matrix"):
    
    matrix = []
    print(f"\nEnter data for {matrix_name}:")
    for i in range(rows):
        while True:
            line = input(f"Enter row {i + 1}: ")
            row = [int(x) for x in line.split()]
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"Error: You must enter exactly {cols} values.")
    return matrix


def transpose_matrix(matrix):
    """Computes the transpose of an M x N matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed



def add_matrices(matrix_A, matrix_B):
    """Computes the element-wise sum of two matrices of identical size."""
    rows = len(matrix_A)
    cols = len(matrix_A[0])
    
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] + matrix_B[i][j]
            
    return result


def multiply_matrices(matrix_A, matrix_B):
    """Multiplies matrix A (M x N) by matrix B (N x P) using nested loops."""
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])  
    cols_B = len(matrix_B[0])
    
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    
    for i in range(rows_A):
        for j in range(cols_B):
            total_sum = 0
            for k in range(cols_A):
                total_sum += matrix_A[i][k] * matrix_B[k][j]
            result[i][j] = total_sum
            
    return result



print("=== PART A: TRANSPOSE A MATRIX ===")
m = int(input("Enter number of rows (M): "))
n = int(input("Enter number of columns (N): "))
matrix_a = read_matrix(m, n, "Original Matrix")

print("\nOriginal Matrix:")
print_matrix(matrix_a)

transposed_a = transpose_matrix(matrix_a)
print("\nTransposed Matrix:")
print_matrix(transposed_a)


print("\n=== PART B: ADD TWO MATRICES ===")
print(f"Reading two matrices of the same size ({m} x {n})...")
mat_B1 = read_matrix(m, n, "Matrix 1")
mat_B2 = read_matrix(m, n, "Matrix 2")

sum_matrix = add_matrices(mat_B1, mat_B2)
print("\nResult of Matrix Addition:")
print_matrix(sum_matrix)


print("\n=== PART C: MULTIPLY TWO MATRICES ===")
print(f"Matrix A size is already set to {m} x {n}.")
mat_C_A = read_matrix(m, n, "Matrix A")

p = int(input(f"Enter number of columns for Matrix B (P) [Rows must be {n}]: "))
mat_C_B = read_matrix(n, p, "Matrix B")

product_matrix = multiply_matrices(mat_C_A, mat_C_B)
print("\nResult of Matrix Multiplication (A × B):")
print_matrix(product_matrix)