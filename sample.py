#183-B (Billiards)

Input = input().split()
Sx = int(Input[0])
Sy = int(Input[1])
Gx = int(Input[2])
Gy = int(Input[3])
X = Gx - Sx
X /= Sy + Gy
X *= Sy
X += Sx
print(X)