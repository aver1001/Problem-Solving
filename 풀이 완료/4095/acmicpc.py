import sys
sys.stdin = open('input.txt', "r")

def boardPrint(board):
    for i in board:
        print(i)
    print()

def solution(board):
    answer = 0
    for y in range (1,Y+1):
        for x in range (1,X+1):
            if board[y][x]:
                board[y][x] = min(board[y-1][x],board[y][x-1],board[y-1][x-1])+1
            else:
                board[y][x] = 0
            answer = max(answer,board[y][x])
    return answer
while True:
    Y, X = map(int, sys.stdin.readline().rstrip().split())
    if Y == 0:
        break
    
    board = [[0]*(X+1)]

    for _ in range (Y):
        board.append([0]+list(map(int,sys.stdin.readline().rstrip().split())))
    print(solution(board))