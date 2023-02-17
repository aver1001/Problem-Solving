import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())
A, B, C, D = [], [], [], []
AB = {}
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split(' '))

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
# 1600만 + 1600만 = 3200만?

for a in A:
    for b in B:
        temp = a+b
        if temp in AB:
            AB[temp] += 1
        else:
            AB[temp] = 1
answer = 0

for c in C:
    for d in D:
        temp = -(c+d)
        if temp in AB:
            answer += AB[temp]


print(answer)
