import sys
sys.stdin = open('input.txt', "r")

N, Q = map(int, sys.stdin.readline().rstrip().split())
record = list(map(int, sys.stdin.readline().rstrip().split(' ')))

table = [0]*(N+1)
for idx in range(N-1):
    table[idx+2] = table[idx+1] ^ record[idx]

for _ in range(Q):
    question = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if question[0] == 0:
        x, y = question[1], question[2]
        print(table[x] ^ table[y])
    else:
        x, y, d = question[1], question[2], question[3]
        print(table[x] ^ table[y] ^ d)
print(table)
