#166-B（Trick or Treat）

#Input
Inputs = []
Input = input().split()

N = Input[0]
N = int(N)
Person = []
for l in range(N):
    Person.append(l+1)

K = Input[1]
K = int(K)
K2 = K * 2
Inputs.append(Input)

for l in range(K2):
    Input = input().split()
    Inputs.append(Input)

#Check
for a in range(K):
    A = (a + 1)*2 
    L = Inputs[A - 1][0]
    L = int(L)
    for b in range(L):
        P = Inputs[A][b]
        P = int(P)
        if P in Person:
            Person.remove(P)

#Output
print(len(Person))
