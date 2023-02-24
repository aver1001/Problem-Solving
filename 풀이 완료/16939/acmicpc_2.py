import sys
from collections import deque
sys.stdin = open('input.txt', "r")

color = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

y1 = deque([color[i] for i in [1,3,5,7,9,11,22,24]])
y2 = deque([color[i] for i in [2,4,6,8,10,12,21,23]])

x1 = deque([color[i] for i in [13,14,5,6,17,18,21,22]])
x2 = deque([color[i] for i in [15,16,7,8,19,20,23,24]])



def moveY():
    yMove()
    isOk()
    
    yMove()
    yMove()
    isOk()
    
    yMove()
    
def moveX():
    xMove()
    isOk()
    
    xMove()
    xMove()
    isOk()
    
    xMove()

def isOk():
    for idx in range (0,8,2):
        # 4면이 같다면
        if y1[idx] == y1[idx+1] == y2[idx] == y2[idx+1] and x1[idx] == x1[idx+1] == x2[idx] == x2[idx+1]:
            continue
        # 하나라도 같지 않다면
        else:
            return
    print(1)
    exit()
        


def printBoard():
    print("Y1 : ",y1)
    print("Y2 : ",y2)
    print("X1 : ",x1)
    print("X2 : ",x2)
    print()
    
'''
y1 = deque([color[i] for i in [1,3,5,7,9,11,22,24]])
y2 = deque([color[i] for i in [2,4,6,8,10,12,21,23]])

x1 = deque([color[i] for i in [13,14,5,6,17,18,21,22]])
x2 = deque([color[i] for i in [15,16,7,8,19,20,23,24]])
'''
def yMove():
    y1.append(y1.popleft())
    y1.append(y1.popleft())
    x1[2] = y1[2]
    x2[2] = y1[3]
    x1[3] = y2[2]
    x2[3] = y2[3]
    
    x1[7] = y1[6]
    x2[7] = y1[7]
    x1[6] = y2[6]
    x2[6] = y2[7]
    
    
def xMove():
    x1.append(x1.popleft())
    x1.append(x1.popleft())

    y1[2] = x1[2]
    y1[3] = x2[2]
    y2[2] = x1[3]
    y2[3] = x2[3]
    
    y1[6] = x1[7]
    y1[7] = x2[7]
    y2[6] = x1[6]
    y2[7] = x2[6]
    
def yxMove():


moveY()
moveX()
print(0)