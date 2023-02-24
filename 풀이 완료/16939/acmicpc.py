import sys
from collections import deque
sys.stdin = open('input.txt', "r")

color = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

y1 = deque([color[i] for i in [1,3,5,7,9,11,22,24]])
y2 = deque([color[i] for i in [2,4,6,8,10,12,21,23]])

x1 = deque([color[i] for i in [13,14,5,6,17,18,21,22]])
x2 = deque([color[i] for i in [15,16,7,8,19,20,23,24]])



def moveY():
    state = False
    y1.append(y1.popleft())
    y1.append(y1.popleft())
    
    ## 맞나 체크
    
    if isOkY():
        state = True
    
    y1.append(y1.popleft())
    y1.append(y1.popleft())
    
    y1.append(y1.popleft())
    y1.append(y1.popleft())

    
    #맞나 체크
    if isOkY():
        state = True
    
    #원상 복귀
    y1.append(y1.popleft())
    y1.append(y1.popleft())
    
    return state
    
def moveX():
    state = False
    x1.append(x1.popleft())
    x1.append(x1.popleft())
    
    ## 맞나 체크
    if isOkX():
        state = True
    
    x1.append(x1.popleft())
    x1.append(x1.popleft())
    
    x1.append(x1.popleft())
    x1.append(x1.popleft())
    
    #맞나 체크
    if isOkX():
        state = True
    x1.append(x1.popleft())
    x1.append(x1.popleft())
    
    return state
def isOkY():
    for idx in range (0,8,2):
        if y1[idx] == y1[idx+1] == y2[idx] == y2[idx+1]:
            continue
        else:
            return False
        
    for idx in (0,4):
        if x1[idx] == x1[idx+1] == x2[idx] == x2[idx+1]:
            continue
        else:
            return False
        
    return True
        
def isOkX():
    for idx in range (0,8,2):
        if x1[idx] == x1[idx+1] == x2[idx] == x2[idx+1]:
            continue
        else:
            return False
        
    for idx in (0,4):
        if y1[idx] == y1[idx+1] == y2[idx] == y2[idx+1]:
            continue
        else:
            return False
        
    return True

def printBoard():
    print("Y1 : ",y1)
    print("Y2 : ",y2)
    print("X1 : ",x1)
    print("X2 : ",x2)
    print()


if moveY()|moveX() :
    print(1)
else:
    print(0)
    
    