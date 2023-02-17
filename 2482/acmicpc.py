import sys
sys.stdin = open('input.txt', "r")

# 서로 인접한 두 색은 사용하지 않는다.
# 서로 이웃하지 않은 색들을 선택하는 경우의 수를 생각해보자

# N개의 색으로 구성되어 있는 색상환에서
# 어떠한 인접한 두 색도 동시에 선택하지 않으면서 서로다른 K개의 색을 선택하는 경우의 수

# 결국 색은 선택하거나 말거나 둘중하나.


N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

table = [[0]*1002 for _ in range(502)]

for i in range(2, 1001):
    table[1][i] = i


for y in range(2, 501):
    for x in range(2, 1001):
        if x//2 < y:
            table[y][x] = 0
        else:
            table[y][x] = (table[y-1][x-2] + table[y][x-1]) % 1000000003


print(table[K][N])
