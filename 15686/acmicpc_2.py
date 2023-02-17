import sys
from itertools import combinations, permutations
import time
sys.stdin = open('input.txt', "r")

# 각 치킨집이랑 집이랑 거리를 한번씩 계산을 다함.
# 집마다 {가게위치: 거리} 를 저장한다
# 치킨집을 제거할수 있는 경우의수를 조합으로 나타낸뒤 빼면서 확인한다

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

house = {}
chicken = set()

for y in range(N):
    board = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for x in range(N):
        # 시작점이 1,1이기떄문에
        # 계산을 편하게 하기위해 +1씩 해줌

        # 집일경우
        if board[x] == 1:
            house[(y+1, x+1)] = []
        elif board[x] == 2:
            chicken.add((y+1, x+1))

for c in chicken:
    for h in house:
        house[h].append([abs(c[0] - h[0]) + abs(c[1] - h[1]), c])
for key in house:
    house[key].sort()

Min = sys.maxsize
for surviveChiken in (combinations(chicken, M)):

    distance = 0
    for values in house.values():
        for v, k in values:
            if k in surviveChiken:
                break
        distance += v

    if Min > distance:
        Min = distance

print(Min)
