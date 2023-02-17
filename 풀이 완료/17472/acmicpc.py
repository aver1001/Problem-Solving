import sys
from collections import deque
import heapq
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

'''
1. 섬의 개수와 위치를 파악한다.
2. 각각의 섬들에서 다리를 만들어서 갈수있는지, 그 거리는 얼만지 찾는다.
3. 최소신장트리를 만들어 연결한다.
'''
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def findIsland():
    # 섬의 개수와 위치를 파악한다.
    island = {}
    check = [[0]*X for _ in range(Y)]
    cnt = 1
    for y in range(Y):
        for x in range(X):
            #안가본곳 + 섬일경우
            if check[y][x] == 0 and board[y][x] == 1:
                pos = [(y, x)]
                check[y][x] = cnt
                queue = deque([(y, x)])
                while queue:
                    y, x = queue.popleft()

                    for idx in range(4):
                        ty = y + dy[idx]
                        tx = x + dx[idx]

                        if 0 <= ty < Y and 0 <= tx < X and check[ty][tx] == 0:
                            if board[ty][tx] == 1:
                                pos.append((ty, tx))
                                check[ty][tx] = cnt
                                queue.append((ty, tx))
                island[cnt] = pos
                cnt += 1

    return check, island


def calDistance():
    N = len(island)
    distance = [[sys.maxsize]*(N) for _ in range(N)]

    for key, value in island.items():
        for y, x in value:
            for idx in range(4):
                ty = y + dy[idx]
                tx = x + dx[idx]

                # 방향을 정해서
                if 0 <= ty < Y and 0 <= tx < X and board[ty][tx] == 0:
                    # 쭉 이동하자.
                    cnt = 1
                    while True:
                        # 방향대로 한칸이동
                        ty += dy[idx]
                        tx += dx[idx]

                        if 0 <= ty < Y and 0 <= tx < X:
                            # 빈곳이 아니고, 내땅도 아닐경우
                            if board[ty][tx] == board[y][x]:
                                break
                            if board[ty][tx] != 0:
                                if cnt == 1:
                                    break
                                distance[board[ty][tx]-1][board[y][x]-1] = min(
                                    cnt, distance[board[ty][tx]-1][board[y][x]-1])
                                distance[board[y][x]-1][board[ty][tx]-1] = min(
                                    cnt, distance[board[y][x]-1][board[ty][tx]-1])
                                break
                            else:
                                cnt += 1
                        else:
                            break
    return distance


def MST():
    heap = []
    answer = 0
    isVisited = [False]*len(island)

    for idx, d in enumerate(distance[0]):
        if d != sys.maxsize:
            heapq.heappush(heap, (d, idx))
    isVisited[0] = True

    while heap:
        dist, idx = heapq.heappop(heap)
        if isVisited[idx] == False:
            isVisited[idx] = True
            answer += dist
            for j, d in enumerate(distance[idx]):
                if d != sys.maxsize and isVisited[j] == False:
                    heapq.heappush(heap, (d, j))

    for state in isVisited:
        if state == False:
            return -1
    else:
        return answer


    # 섬의 개수와 위치를 파악한다.
board, island = findIsland()
# 각각의 섬들에서 다리를 만들어서 갈수있는지, 그 거리는 얼만지 찾는다.
distance = calDistance()
# 최소신장트리를 만들어 연결한다.
print(MST())
