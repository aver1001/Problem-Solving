import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))
table = [0]*N

for i in range(N):
    for j in range(i+1):
        table[i] = max(abs(commend[i] - commend[j]) + table[j-1], table[i])

print(table[-1])
