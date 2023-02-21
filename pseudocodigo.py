def puzzle(N):
    A = 1
    B = 1
    C = 1
    D = 1
    for i in range(N):
        X = D + 2 * C + 3 * B + 4 * A
        A = B
        B = C
        C = D
        D = X
    return D % 10000000000

print(puzzle(10))
print(puzzle(100))
print(pow(2022, 100))

