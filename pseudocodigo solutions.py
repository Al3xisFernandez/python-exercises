import numpy as np
def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    n, m = A.shape
    m, p = B.shape
    C = np.zeros((n, p), dtype=int)
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]
                C[i, j] %= 10**10
    return C

def puzzle(N):
    import numpy as np

    M = np.array([[0, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [4, 3, 2, 1]], dtype=int)
    X = np.array([1, 1, 1, 1], dtype=int)

    # Use exponentiation by squaring to compute M^N
    while N > 0:
        if N % 2 == 1:
            X = matrix_multiply(M, X)
        M = matrix_multiply(M, M)
        N //= 2

    return X[3]

print(puzzle(10))              
print(puzzle(100))            
print(puzzle(pow(2022, 100)))  
