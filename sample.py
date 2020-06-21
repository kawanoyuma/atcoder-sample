#170-B (Crane and Turtle)

Input = input().split()
X = Input[0]
X = int(X)
Y = Input[1]
Y = int(Y)

A = 0
for i in range(X+1):
    C = i
    T = X - C
    CL = C * 2
    TL = T * 4
    L = CL + TL
    if L == Y:
        A += 1

if A == 0:
    print("No")
else:
    print("Yes")