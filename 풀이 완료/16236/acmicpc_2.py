from operator import ne
import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
N N 크기의 공간에 물고기 M 마리와 아기상어 한마리가 있습니다.

처음에 아기 상어의 크기는 2 이고 아기상어는 1초마다 상하좌우로 인접한 한칸씩 이동합니다.
아기상어는 자신보다 작거나 같은 물고기만 먹을 수 있습니다.
거리가 가까운 물고기가 많다면, 가장 위에있는 물고기, 가장 왼쪽에 있는 물고기 순으로 먹습니다

아기상어는 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1증가한다.
'''

# 일단 거리는 계속 바뀔것이기 때문에 계속 갱신해줘야함.
# 공간의 크기가 최대 20 * 20이기때문에 다 갱신해줘도 괜찮을것으로 예상됨

#
N = int(sys.stdin.readline().rstrip())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

fish = {
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set()
}
for y in range(N):
    for x in range(N):
        if board[y][x] in [1, 2, 3, 4, 5, 6]:
            fish[board[y][x]].add((y, x))
        elif board[y][x] == 9:
            board[y][x] = 0
            shark = (y, x)

sharkSize = 2
sharkCnt = sharkSize
canEat = True
time = 0


def BFS(y, x):
    queue = deque([[y, x, 0]])
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    check = [[0]*N for _ in range(N)]
    temp = []
    minDis = 999999
    while queue:
        y, x, cnt = queue.popleft()

        if minDis < cnt:
            break
        # 만약 물고기였는데
        if 0 < board[y][x] < sharkSize:
            temp.append([cnt, y, x])
            minDis = cnt
            continue
        for idx in range(4):
            ty = y+dy[idx]
            tx = x+dx[idx]

            # 범위를 벗어나지않고
            if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0 and cnt+1 <= minDis:
                # 지나갈 수 있을경우 지나가준다
                if board[ty][tx] <= sharkSize:
                    check[ty][tx] = 1
                    queue.append([ty, tx, cnt+1])
    if temp:
        temp.sort(key=lambda x: (x[0], x[1], x[2]))
        return temp[0][1], temp[0][2], temp[0][0]
    else:
        return -1, -1, -1


while True:

    # 먹을수 있는게 있는지 확인
    for idx in range(1, sharkSize+1):
        if idx >= 7:
            continue
        if len(fish[idx]) != 0:
            canEat = True

    if canEat:
        # 조건에 맞는 물고기를 찾아주고, 시간까지 가져옴
        y, x, nextTime = BFS(*shark)
        if y == -1:
            break
        if y == 25:
            break
        time += nextTime  # 시간을 더해주고
        shark = (y, x)
        # 물고기 set에서 삭제
        fish[board[y][x]].remove((y, x))
        sharkCnt -= 1
        if sharkCnt == 0:
            sharkSize += 1
            sharkCnt = sharkSize
        board[y][x] = 0
        board[shark[0]][shark[1]] = 'S'
        board[shark[0]][shark[1]] = 0
        # 더이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 어마 상어에게 도움을 청한다.
    else:
        break

print(time)
