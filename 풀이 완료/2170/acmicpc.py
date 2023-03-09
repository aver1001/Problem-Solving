import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
score = []
for idx in range (N):
    X, Y = map(int, sys.stdin.readline().rstrip().split())
    score.append((X,Y))
score.sort()

bX = -sys.maxsize
bY = -sys.maxsize
answer = 0
#print(score)
for (X,Y) in score:
    # 이전거랑 겹치지 않을경우
    if bY < X:
        answer += Y-X
        bX = X
        bY = Y
    # 이전거랑 일부 겹칠경우
    elif X <= bY and bY < Y:
        answer += Y-bY
        bX = X
        bY = Y
    # 이전거 안에 있을경우
    elif bX < X and bY > Y:
        bX = X

    
    #print(answer)
    
print(answer)
