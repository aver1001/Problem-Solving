from calendar import c
import sys
sys.stdin = open('input.txt', "r")
'''
왼쪽위 1,1
맨위랑 맨 아래랑 연결되어있음
오른쪽 왼쪽도 연결되어있음

비바라기를 시전하면 
왼쪽아래 2X2 비구름이 생성됨

i번쨰 이동 명령은 방향 d와 거리 s로 이루어져있음

'''

# 모든 구름이 di방향으로 si칸 이동한다.
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물이 1 증가한다
# 구름이 모두 사라진다
# 물이 증가한 칸에 물복사버그 마법을 시전함
'''
대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼 바구니의 물의 양이 증가한다
'''
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 곳은 전에 구름이 사라진 칸이 아니여야함.

direct = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

# 비구름 배열을 만들어놓고 각자 조정한다
# 처음 구름은 왼쪽 아래에 4칸 존재하기때문에 초기화
cloud = [[N-1, 0], [N-2, 0], [N-1, 1], [N-2, 1]]


def printBoard():
    for i in board:
        print(i)
    print()


for _ in range(M):

    d, s = map(int, sys.stdin.readline().rstrip().split(' '))
    d -= 1
    checkCloud = set()

    for idx in range(len(cloud)):
        # 이동
        cloud[idx][0] += direct[d][0] * s
        cloud[idx][1] += direct[d][1] * s
        # 넘어가는거 이어줘야함
        cloud[idx][0] %= N
        cloud[idx][1] %= N
        # 도착한곳에 물 증가 +1
        board[cloud[idx][0]][cloud[idx][1]] += 1
        checkCloud.add((cloud[idx][0], cloud[idx][1]))

    addWater = []
    for y, x in cloud:
        cnt = 0
        # 물복사 마법 시전
        for addy, addx in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            ty = y+addy
            tx = x+addx

            if 0 <= ty < N and 0 <= tx < N and board[ty][tx] > 0:
                cnt += 1
        addWater.append([y, x, cnt])
    cloud = []
    for y, x, cnt in addWater:
        board[y][x] += cnt

    for y in range(N):
        for x in range(N):
            if board[y][x] >= 2 and (y, x) not in checkCloud:
                board[y][x] -= 2
                cloud.append([y, x])

answer = 0
for i in board:
    answer += sum(i)
print(answer)
