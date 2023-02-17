import sys
sys.stdin = open('input.txt', "r")

N, M, H = map(int, sys.stdin.readline().rstrip().split(' '))

initLadder = set()
canLadder = set()
for y in range(H):
    for x in range(N-1):
        canLadder.add((y, x))

for _ in range(M):
    y, x = map(int, sys.stdin.readline().rstrip().split(' '))
    y -= 1
    x -= 1
    initLadder.add((y, x))
    # 초기 사다리 초기화 하면서
    # 우리가 만들수 있는 사다리들을 정리해준다
    if (y, x) in canLadder:
        # 만든 사다리를 만들수 있는 사다리에서 제거해주고
        canLadder.remove((y, x))

        # 경우의 따라서 좌우 사다리도 제거해준다 => 사다리가 가로로 연속할수 없다는 조건
        if x == 0:
            if (y, x+1) in canLadder:
                canLadder.remove((y, x+1))
        elif x == H-2:
            if (y, H-3) in canLadder:
                canLadder.remove((y, M-3))
        else:
            if (y, x+1) in canLadder:
                canLadder.remove((y, x+1))
            if (y, x-1) in canLadder:
                canLadder.remove((y, x-1))


def isStraight(initLadder, bulidLadder):
    for start in range(N):
        y, x = 0, start
        while True:
            if x == H:
                break

            # 왼쪽 확인
            if x - 1 >= 0 and ((x-1, y) in initLadder or (x-1, y) in bulidLadder):


print(initLadder)
print(canLadder)
