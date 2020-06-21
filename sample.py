#170-C (Forbidden List)

Input = input().split()
X = Input[0]
X = int(X)
N = Input[1]
N = int(N)
if N != 0:
    P = input().split()
    Z = 0
    A = 0
    while Z < 1:
        B = X + A
        C = X - A
        B = str(B)
        C = str(C)
        if not(C in P):
            D = C
            Z = 1
            break
        if not(B in P):
            D = B
            Z = 1
            break
        A += 1
else:
    D = X

print(D)