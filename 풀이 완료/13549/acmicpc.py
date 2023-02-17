import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

# BFS OR DP


def DP(start, end):
    table = [-1]*(100001)

    queue = deque([[start, 0]])
    while queue:
        nowLoc, nowCost = queue.popleft()
        if table[nowLoc] > nowCost or table[nowLoc] == -1:
            table[nowLoc] = nowCost
        else:
            continue

        for nextLoc, nextCost in [[nowLoc*2, nowCost], [nowLoc+1, nowCost+1], [nowLoc-1, nowCost+1]]:

            if 0 <= nextLoc < (100001) and (table[nextLoc] > nextCost or table[nextLoc] == -1):
                queue.append([nextLoc, nextCost])
    return table[end]


print(DP(N, K))
