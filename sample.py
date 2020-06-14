#169-B（Multiplication2）

N = input()
N = int(N)
A = input().split()

minA = min(A)
minA = int(minA)
M = 10 ** 18

Y = 0
if minA != 0:
    Y = 1
    for i in range(N):
        X = A[i]
        X = int(X)
        Y = Y * X
        if Y > M:
            break


if Y > M:
    print(-1)
else:
    print(Y)