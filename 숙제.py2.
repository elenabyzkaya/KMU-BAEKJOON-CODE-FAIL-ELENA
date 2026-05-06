import random

def generate_matrix(n):
    limit = n * n * 10
    return [[random.randint(1, limit - 1) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix, name):
    print(f"\n[{name}]")
    for row in matrix:
        for val in row:
            print(f"{val:4}", end=" ")
        print()

def solve_2():
    n = int(input("Enter N (1 < N <= 5): "))
    if not (1 < n <= 5):
        print("Invalid input!")
        return

    A = generate_matrix(n)
    
    # Transpose Operation
    transpose_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpose_matrix[j][i] = A[i][j]

    print_matrix(A, "Original Matrix A")
    print_matrix(transpose_matrix, "Transposed Matrix A")

solve_2()
