import sys
sys.stdin = open('input.txt', "r")

N, H = map(int, sys.stdin.readline().rstrip().split(' '))

table = [0]*(H+2)

cnt = 0
for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())

    # 바닥
    if cnt % 2 == 0:
        table[1] += 1
        table[temp+1] -= 1
    # 천장
    else:
        table[H-temp+1] += 1
        table[H+1] -= 1

    cnt += 1

for idx in range(1, H+2):
    table[idx] = table[idx-1] + table[idx]

Min = min(table[1:-1])
print(Min, table.count(Min))
