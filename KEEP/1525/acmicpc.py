import sys
from collections import deque
sys.stdin = open('input.txt', "r")
board = []

for _ in range(3):
    board.append(list(sys.stdin.readline().rstrip().split(' ')))

check = set()
change = {0: (1, 3),
          1: (0, 2, 4),
          2: (1, 5),
          3: (0, 4, 6),
          4: (1, 3, 5, 7),
          5: (2, 4, 8),
          6: (3, 7),
          7: (4, 6, 8),
          8: (5, 7)
          }
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def posChange(board):
    temp = ''
    for y in range(3):
        for x in range(3):
            temp = temp + str(board[y][x])
    return temp


queue = deque([[posChange(board), 0]])


while queue:
    pos, cnt = queue.popleft()
    if pos == '123456780':
        print(cnt)
        exit()

    # 중복 검사
    if pos in check:
        continue
    else:
        check.add(pos)

    # 리스트로 변경 후
    temp = list(pos)
    # 변화하는거 체크
    zeroIdx = temp.index('0')
    for c in change[zeroIdx]:
        # 두개 자리 바꿔주고
        temp[c], temp[zeroIdx] = temp[zeroIdx], temp[c]
        # 다음큐에 넣어줌
        checktemp = ''.join(temp)
        if checktemp not in check:
            queue.append((checktemp, cnt+1))
        # 원상복귀
        temp[c], temp[zeroIdx] = temp[zeroIdx], temp[c]

print(-1)
