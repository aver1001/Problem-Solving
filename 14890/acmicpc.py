import sys
sys.stdin = open('input.txt', "r")

N, L = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


'''
올라가는건 안됨.
내려가는건 1칸만 가능하며 그게 연속으로 L 번 연속되어야 진행가능.
'''
answer = 0


def isWalk(loc):
    global answer

    cross = [False]*N
    for x in range(N-1):
        #다음칸이 +1
        if board[loc][x]-board[loc][x+1] == -1:
            # 오르막 => 나포함 뒤에 L칸 확인
            for c in range(x, x-L, -1):
                if 0 <= c < N and board[loc][c] == board[loc][x] and cross[c] == False:
                    cross[c] = True
                else:
                    break
            else:
                continue
        # 다음칸이  0
        elif board[loc][x]-board[loc][x+1] == 0:
            continue
        # 내리막 => 나 뺴고 앞에 두칸 확인
        elif board[loc][x]-board[loc][x+1] == 1:

            for c in range(x+1, x+L+1):
                if 0 <= c < N and board[loc][c] == board[loc][x+1] and cross[c] == False:
                    cross[c] = True
                else:
                    break
            else:
                continue

        break
    else:
        answer += 1

    cross = [False]*N
    temp = []
    for y in range(N-1):
        temp.append(board[y][loc])
        #다음칸이 +1
        if board[y][loc]-board[y+1][loc] == -1:
            # 내칸포함해서 뒤로 L개 값이 같은지 확인 하며 경사로 지은게 없는거 확인
            for c in range(y, y-L, -1):
                if 0 <= c < N and board[y][loc] == board[y][loc] and cross[c] == False:
                    cross[c] = True
                    continue
                else:

                    break
            else:
                continue
        # 다음칸이  0
        elif board[y][loc]-board[y+1][loc] == 0:
            continue
        # 다음칸이 -1
        elif board[y][loc]-board[y+1][loc] == 1:
            for c in range(y+1, y+L+1):
                if 0 <= c < N and board[c][loc] == board[y+1][loc] and cross[c] == False:
                    cross[c] = True
                    continue
                else:
                    break
            else:
                continue
        break
    else:
        answer += 1


for i in range(N):
    isWalk(i)

print(answer)
