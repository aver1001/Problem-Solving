import sys
sys.stdin = open('input.txt', "r")
# 6,2
wheel = []
wheelState = [[6, 2], [6, 2], [6, 2], [6, 2]]
for _ in range(4):
    wheel.append(list(sys.stdin.readline().rstrip()))

K = int(sys.stdin.readline().rstrip())


def changeWheel(idx, direct, lr):
    # 만약 극이 다르다면 움직여줘야함
    if idx - 1 >= 0 and wheel[idx][wheelState[idx][0]] != wheel[idx-1][wheelState[idx-1][1]] and lr <= 0:
        changeWheel(idx-1, -direct, -1)
    if idx + 1 < 4 and wheel[idx][wheelState[idx][1]] != wheel[idx+1][wheelState[idx+1][0]] and lr >= 0:
        changeWheel(idx+1, -direct, 1)

    if direct == -1:
        # 반시계방향
        wheelState[idx][0] = (wheelState[idx][0] + 1) % 8
        wheelState[idx][1] = (wheelState[idx][1] + 1) % 8

    elif direct == 1:
        # 시계방향
        wheelState[idx][0] = (wheelState[idx][0] - 1) % 8
        wheelState[idx][1] = (wheelState[idx][1] - 1) % 8


def calScore():
    answer = 0
    for idx in range(4):
        if wheel[idx][(wheelState[idx][1] - 2) % 8] == '1':
            answer += 2**(idx)
    return answer
# N극이 0 S극이 1
# 1번 12시가 S면 1점
# 2번 12시가 S면 2점
# 3번 12시가 S면 4점
# 4번 12시가 S면 8점


for idx in range(K):
    num, direct = map(int, sys.stdin.readline().rstrip().split(' '))
    num -= 1

    changeWheel(num, direct, 0)

print(calScore())
