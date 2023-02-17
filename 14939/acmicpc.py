import sys
from copy import deepcopy
sys.stdin = open('input.txt', "r")

check = set()

board = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    line = sys.stdin.readline()
    for j in range(len(line)):
        if line[j] == "O":
            board[i][j] = 1


'''
우리가 원하는 위치의 불을 끄는 방법은 5가지가 있다.
(상 하 좌 우 원점 의 불을 끄고 키는 방법)
정황상 다 브루드포스에서 DP 설정해준뒤 백트레킹 하는 방법이 맞는 것 같음.

DP 를 설정하려면 어떻게 설정 해야할까
board 상태를 저장하고, 이 상태가 없었을 경우만 진행하는게 좋을거 같음.

근데 경우의수가 2^100 이기떄문에 DP배열을 만들면 메모리 우주초과 날거같음..
어차피 정황상 모든 경우를 다 접근할수는 없는 것같음.
그럼 현재 상태를 저장해놓는게 좋을거 같음..
일단 메모리 아낄려면 다른방법으로 저장하는게 좋을거 같은데 가능한지 확인해보기 위해서 그냥 board 자체를 저장 해 보겠음.

'''
def in_range(y, x): return 0 <= y < 10 and 0 <= x < 10


dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]


def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if in_range(ny, nx):
            b[ny][nx] = (b[ny][nx] + 1) % 2


direct = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 999
for case in range(1024):
    temp_board = deepcopy(board)
    cnt = 0

    mask = 1
    for i in range(9, -1, -1):
        # 만약 불을 켜야하면
        if case & mask:
            press(temp_board, 0, i)
            cnt += 1
        mask <<= 1

    for y in range(1, 10):
        for x in range(10):
            if temp_board[y-1][x]:
                press(temp_board, y, x)
                cnt += 1

    isDoIt = True
    for i in temp_board[-1]:
        if i == True:
            isDoIt = False
            break

    if isDoIt:
        answer = min(answer, cnt)

print(answer)
