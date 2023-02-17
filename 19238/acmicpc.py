import sys
from collections import deque
sys.stdin = open('input.txt', "r")

'''
현재 위치에서 최단거리가 가장 짧은 고객을 고름
만약 거리가 같다면 행번호가 작은순, 열번호가 작은순으로 고른다

연료는 이동할떄마다 1씩 감소한다.
한 승객을 목적지로 성공적으로 도착시키면 소모한 연료의 두배가 충전된다.

모든손님을 이동시키고 연료를 충전했을떄 남은 연료의 양을 출력한다.
단 모두 이동시킬 수 없다면 -1 을 출력한다.

'''

# N == board size, M == 승객의 수
N, M, fuel = map(int, sys.stdin.readline().rstrip().split(' '))
board = []  # 0은 빈칸 1은 벽
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
y, x = map(int, sys.stdin.readline().rstrip().split(' '))
y -= 1
x -= 1

person = {}
for _ in range(M):
    beforeA, beforeB, afterA, afterB = map(
        int, sys.stdin.readline().rstrip().split(' '))

    person[(beforeA-1, beforeB-1)] = (afterA-1, afterB-1)

'''
BFS 돌려서 도착한 위치에 승객이 있으면 태운다.
단 거리가 같을경우를 생각해야함.
'''
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while True:

    queue = deque([(y, x, 0)])
    check = [[0]*(N) for _ in range(N)]
    check[y][x] = 0
    peopleLoc = []
    minLoc = 100
    isFind = False

    if (y, x) in person:
        minLoc = 0
        peopleLoc.append((y, x))
    else:
        while queue:
            moveY, moveX, cnt = queue.popleft()
            if cnt >= minLoc:
                continue

            for idx in range(4):
                ty = moveY + dy[idx]
                tx = moveX + dx[idx]
                # 가보지 않은곳 and 벽이 아닐경우 and 범위 안나갔을경우
                if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0 and board[ty][tx] == 0:
                    check[ty][tx] = cnt+1
                    # 이 위치에 승객이 있을경우
                    if (ty, tx) in person:
                        peopleLoc.append((ty, tx))
                        # 처음 승객을 만났을경우
                        if isFind == False:
                            # 만난거 표시 해주고
                            isFind = True
                            minLoc = cnt + 1
                    # 이미 승객을 만났다면 더이상 추가하지 말고 있는거에서 찾아야함.
                    if isFind == False:
                        queue.append((ty, tx, cnt + 1))

    # 연료 처리
    if minLoc == 100:
        break
    fuel -= minLoc

    # 행,열 순서로 정렬해주고
    peopleLoc.sort(key=lambda x: (x[0], x[1]))
    target = person[peopleLoc[0]]
    queue = deque([(*peopleLoc[0], 0)])
    check = [[0]*(N) for _ in range(N)]
    check[y][x] = '0'

    while queue:

        y, x, cnt = queue.popleft()
        for idx in range(4):
            ty = y + dy[idx]
            tx = x + dx[idx]
            # 가보지 않은곳 and 벽이 아닐경우 and 범위 안나갔을경우
            if 0 <= ty < N and 0 <= tx < N and check[ty][tx] == 0 and board[ty][tx] == 0:
                if (ty, tx) == target:
                    break
                queue.append((ty, tx, cnt+1))
                check[ty][tx] = cnt+1
    if len(queue) == 0:
        print(-1)
        exit()
    # 연료 처리
    if fuel - cnt <= 0:
        break

    fuel += cnt-1

    # 도착한 위치의 사람 삭제
    # print(peopleLoc[0], '삭제 ')
    # print('남은 연료', fuel)
    del person[peopleLoc[0]]
    y, x = ty, tx

if len(person) == 0:
    print(fuel)
else:
    print(-1)
