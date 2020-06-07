#116-B（Collatz Problem）
a = []
s = input()
s = int(s)
a.append(s)

i = 0
while i <= 1000000:
    n = a[-1]
    n = int(n)
    if n % 2 == 0:
        C = n / 2
    else:
        C = n * 3 + 1
    if C in a:
        a.append(C)
        break
    a.append(C)
print(len(a))