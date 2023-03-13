import sys
from copy import deepcopy
import time
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
userList = list(map(int,sys.stdin.readline().rstrip().split(' ')))

answer = 0
while True:
    if len(userList) <= 1:
        break
    
    maxIdx = userList.index(max(userList))
    
    if maxIdx == len(userList)-1:
        answer += abs(userList[maxIdx] - userList[-2])
        userList.pop(maxIdx)
        
    elif maxIdx == 0:
        answer += abs(userList[1] - userList[maxIdx])
        userList.pop(maxIdx)
    else:
        if abs(userList[maxIdx-1] - userList[maxIdx]) < abs(userList[maxIdx+1] - userList[maxIdx]):
            answer += abs(userList[maxIdx-1] - userList[maxIdx])
            userList.pop(maxIdx)
        else:
            answer += abs(userList[maxIdx+1] - userList[maxIdx])
            userList.pop(maxIdx)
            
print(answer)