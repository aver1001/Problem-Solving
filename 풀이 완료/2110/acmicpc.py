import sys
sys.stdin = open('input.txt', "r")

N, C = map(int, sys.stdin.readline().rstrip().split(' '))
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()
'''
한집에 하나만 공유기를 설치 할 수 있다.
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치한다.
'''

lt, rt = 0, 1_000_000_000
while lt <= rt:

    mid = (lt+rt) // 2

    houseCnt = C-1
    nowLoc = house[0]
    for idx in range(1, N):

        if houseCnt == 0:
            break

        if house[idx] - nowLoc >= mid:
            houseCnt -= 1
            nowLoc = house[idx]

    # 다 설치 못햇음
    if houseCnt > 0:

        rt = mid - 1
    else:
        answer = mid
        lt = mid + 1

print(answer)
