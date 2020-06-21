#170-A (Five Variables)

Input = input().split()

X = 0
for i in range(5):
    M = Input[i]
    M = int(M)
    N = i + 1
    if M != N:
        X = N

print(X)