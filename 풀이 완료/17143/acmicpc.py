import sys
sys.stdin = open('input.txt', "r")

Y, X, M = map(int, sys.stdin.readline().rstrip().split(' '))
shark = {}
for _ in range(M):
    # y,x,속력,이동방향(1:위,2:아래,3:오른쪽,4:왼쪽),크기
    y, x, speed, direct, size = map(
        int, sys.stdin.readline().rstrip().split(' '))
    shark[(y-1, x-1)] = [speed, direct, size]


def fishing(now):
    for idx in range(Y):
        if (idx, now) in shark:
            temp = shark[(idx, now)][2]
            print(temp, 'size shark get')
            del shark[(idx, now)]
            return temp
    return 0


def moveAllFish():
    afterShark = {}
    for key, value in shark.items():
        y, x = key
        speed, direct, size = value
        # 물고기 이동
        y, x, direct = moveOneFish(y, x, speed, direct, size)
        # 이미 다음 위치에 물고기가 존재할 경우
        if (y, x) in afterShark:
            # 지금 물고기가 더 클경우
            if size > afterShark[(y, x)][2]:
                afterShark[(y, x)] = [speed, direct, size]
        # 다음 위치에 물고기가 없을 경우
        else:
            afterShark[(y, x)] = [speed, direct, size]

    return afterShark


def moveOneFish(y, x, speed, direct, size):
    # 위
    if direct == 1:
        speed = speed % (Y*2 - 2)
        # 넘어가 버리면
        if y-speed < 0:
            return moveOneFish(0, x, -(y-speed), 2, size)
        else:
            return (y-speed, x, direct)
    # 아래
    elif direct == 2:
        speed = speed % (Y*2 - 2)
        # 넘어가 버리면
        if y+speed >= Y:
            return moveOneFish(Y-2, x, (y+speed-Y), 1, size)
        else:
            return (y+speed, x, direct)
    # 오른쪽
    elif direct == 3:
        speed = speed % (X*2 - 2)
        # 넘어가 버리면
        if x+speed >= X:
            return moveOneFish(y, X-2, (x+speed-X), 4, size)
        else:
            return (y, x+speed, direct)
    # 왼쪽
    elif direct == 4:
        speed = speed % (X*2 - 2)
        # 넘어가 버리면
        if x-speed < 0:
            return moveOneFish(y, 0, -(x-speed), 3, size)
        else:
            return (y, x-speed, direct)


answer = 0
for idx in range(X):
    answer += fishing(idx)
    shark = moveAllFish()
print(answer)
