from os import kill
import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

'''
성을 지키기 위해 궁수 3명을 배치하려고 한다.
궁수는 성이 있는 칸에 배치

각턴마다 궁수는 하나의 적을 공격할 수 있으며 모든 궁수는 동시에 공격한다.
궁수는 거리가 D이하인 적 중에서 가장 가까운적을 공격하며, 왼쪽부터 공격한다.

공격받은 적은 게임에서 제외된다

궁수의 공격이 끝나면 적이 이동한다.
적은 아래로 한칸 이동하며 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다.
모든 적이 격자판에서 제외되면 게임이 끝난다
'''

Y, X, D = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(Y):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def Attack(archorLoc):
    answer = 0

    killedEnemy = set()
    for y in range(Y, 0, -1):
        # 아처 위치 순회하면서
        nowkill = set()
        for archor in archorLoc:
            # 삭제조건에 맞는 적을 찾아줌
            ky, kx = killEnemy(y, archor, killedEnemy)
            # set에 넣어줘서 중복을 제거하며 넣어줌
            if kx != 2000:
                nowkill.add((ky, kx))

        for temp in nowkill:
            killedEnemy.add(temp)
            answer += 1

    return answer


def killEnemy(ay, ax, killedEnemy):
    answer = [[1, 2000, 9999999]]

    for y in range(-D, 0):
        for x in range(-D, D+1):
            dist = abs(y)+abs(x)
            if dist > D:
                continue

            ty = y+ay
            tx = x+ax

            if 0 <= tx < X and 0 <= ty < Y and board[ty][tx] == 1 and (ty, tx) not in killedEnemy:
                if answer[0][2] > dist:
                    answer = [[ty, tx, dist]]
                elif answer[0][2] == dist:
                    answer.append([ty, tx, dist])

    answer.sort(key=lambda x: (x[1]))
    return answer[0][0], answer[0][1]


archorLoc = combinations(range(X), 3)
answer = 0
for archor in archorLoc:
    answer = max(answer, Attack(archor))

print(answer)
