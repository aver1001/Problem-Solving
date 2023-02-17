import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
point = []
for _ in range (N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    point.append((x1,y1,x2,y2))

'''
n^2이 가능함.
그렇다면 각각 좌표가 연결되어있는지를 확인 후 순환하는지 확인하면 되는거 아님?
'''

def ccw(x1,y1,x2,y2,x3,y3):
    '''
    신발끈 공식 사용
    x1 y1
    x2 y2
    x3 y3
    x1 y1
    '''
    temp = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1
    
def isCross(x1,y1,x2,y2,x3,y3,x4,y4):
    temp1 = ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)
    temp2 = ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)
    if temp1 == temp2 == 0:
        #두 선분이 평행할경우
        if (x1,y1) > (x2,y2):
            x1,y1,x2,y2 = x2,y2,x1,y1
        if (x3,y3) > (x4,y4):
            x3,y3,x4,y4 = x4,y4,x3,y3
            
        if (x1,y1) <= (x4,y4) and (x3,y3) <= (x2,y2):
            return True
        else:
            return False
            
    elif temp1 <= 0 and temp2 <= 0:
        return True
    else:
        return False

table = {i : [] for i in range (N)}
for i,j in combinations(range(N),2):
    if isCross(*point[i],*point[j]):
        table[i].append(j)
        table[j].append(i)
isVisited = [False]*N
answer = 0
cnt = 0
for i in range (N):
    if isVisited[i] == False:
        temp = 0
        cnt += 1
        queue = deque([i])
        while queue:
            Loc = queue.popleft()
            if isVisited[Loc] == True:
                continue
            temp += 1
            isVisited[Loc] = True
            
            for nextLoc in table[Loc]:
                if isVisited[nextLoc] == False:
                    queue.append(nextLoc) 
        
        answer = max(answer,temp)
print(cnt)
print(answer)