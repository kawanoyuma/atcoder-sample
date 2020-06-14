#169-D (Div Game)

#入力
N = input()
N = int(N)

#素因数分解
Num = []
n = N
for i in range(2, int(-(-N**0.5//1))+1):
    if n%i==0:
        j=0
        while n%i==0:
            j+=1
            n //= i
        Num.append(j)

if n!=1:
    Num.append(1)

if Num==[]:
    if N == 1:
        Num.append(0)
    else:
        NUm.append(1)

#階差数列
P = []
p = 0
l = max(Num)
for i in range(1,l+1):
    p += i
    P.append(p)

#計算
Answer = 0

l = len(Num)

if Num[0] != 0:
    for i in range(l):
        q = Num[i]
        while not(q in P):
            q -= 1
        Index = P.index(q)
        Index = int(Index)
        Index += 1
        Answer += Index

#出力
print(Answer)