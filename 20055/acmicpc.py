import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
각 칸에는 내구도가 있음
시계방향으로 돌고
왼쪽위를 올리는위치 오른쪽위를 내리는 위치라고 함
로봇은 올리는 위치에만 올릴 수 있음
내리는 위치에 도착하면 즉시 내림
로봇은 컨베이너 벨트 위에서 스스로 이동 할 수 있음.
로봇을 올리는 위치에 올리거나 이동하면 그 칸의 내구도 1 감소

1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전한다.
2. 가장 먼저 벨트에 올리간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동
    1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아있어야함.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올림
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료

'''
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split(' ')))

upBelt = deque([])
downBelt = deque([])
global zeroCnt
zeroCnt = 0

for idx in range(N*2):
    # [내구도, 로봇의 존재여부]
    if idx < N:
        upBelt.append([A[idx], False])
    else:
        downBelt.appendleft([A[idx], False])

    # 내구도 0 개수 확인용
    if A[idx] == 0:
        zeroCnt += 1

# 벨트가 각 칸 위에 잇는 로봇과 함께 한칸 회전한다


def stepOne():
    # 위에 오른쪽 빼서 아래 오른쪽 넣어줌
    downBelt.append(upBelt.pop())
    # 아래 왼쪽 빼서 위 왼쪽 넣어줌
    upBelt.appendleft(downBelt.popleft())

    # 내리는 위치 벨트에 로봇잇으면 내려주기
    if upBelt[-1][1] == True:
        upBelt[-1][1] = False


def stepTwo():
    global zeroCnt
    # 가장 먼저 벨트에 올리간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.

    # upBelt의 가장 오른쪽이 가장 먼저 올라간 로봇 일 것임.
    # 가장 오른쪽은 내리는 위치이기때문에 항상 비어있을것.
    # 그래서 -2인덱스부터 확인하면됨
    for idx in range(N-2, -1, -1):
        # 조건 만족한다면(내벨트에 로봇이 있고 AND 다음벨트에 로봇이 없고 AND 다음벨트 내구도가 1이상일경우)
        if upBelt[idx][1] and upBelt[idx+1][1] == False and upBelt[idx+1][0] >= 1:
            # 로봇 옮겨주기
            upBelt[idx][1] = False
            upBelt[idx+1][1] = True
            # 내구도 줄여주기
            upBelt[idx+1][0] -= 1

            # 내구도 0되었으면 체크
            if upBelt[idx+1][0] == 0:
                zeroCnt += 1

    # 내리는 위치에 로봇 잇는지 확인 후 내려주기
    if upBelt[-1][1] == True:
        upBelt[-1][1] = False


def stepThree():
    global zeroCnt

    # 올리는 위치의 칸에 내구도가 0이 아니라면
    if upBelt[0][0] != 0:
        # 로봇 올려주고 내구도 줄여주기
        upBelt[0][1] = True
        upBelt[0][0] -= 1

        # 내구도 0된거 확인
        if upBelt[0][0] == 0:
            zeroCnt += 1


def stepFour():
    # Break 조건 확인
    if zeroCnt >= K:
        return False
    else:
        return True


def printBelt():
    print(upBelt)
    print(downBelt)
    print(zeroCnt)
    print()


answer = 1
while True:
    stepOne()
    stepTwo()
    stepThree()
    if stepFour() == False:
        break
    answer += 1

print(answer)
