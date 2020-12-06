#184-B (Quizzes)

NX = input().split()
S = list(input())
N = int(NX[0])
X = int(NX[1])
P = X
for i in range(N):
    if S[i] == "o":
        P += 1
    else:
        if P!=0:
            P -= 1
print(P)