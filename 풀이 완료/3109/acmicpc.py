import sys
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))

board = []
for _ in range(Y):
    board.append(list(sys.stdin.readline().rstrip()))


def printBoard():
    for i in board:
        print(i)
    print()


def DFS(y, x):

    # 마지막까지 잘 도착했으므로 파이프라인 설치
    if x == X-1:
        return True

    # 오른쪽위, 오른쪽, 아래 순으로 설치해본다.
    # 설치 해본곳은 O를 넣어 구분해주고 설치 가능할경우 True return
    for add in [-1, 0, 1]:
        ty = y + add
        if 0 <= ty < Y and board[ty][x+1] == '.':
            board[ty][x+1] = 'O'
            state = DFS(ty, x+1)
            if state == True:
                return True

    return False


answer = 0

for y in range(Y):
    if board[y][0] != 'x':

        if DFS(y, 0):
            answer += 1

print(answer)
