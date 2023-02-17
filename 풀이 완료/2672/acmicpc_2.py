import sys
from decimal import Decimal
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
rec = []

for _ in range (N):
    x,y,w,h = map(float,sys.stdin.readline().rstrip().split())
    y = int(y*10)
    x = int(x*10)
    w = int(w*10)
    h = int(h*10)
    #x축으로 봤을때 시작점 (x,y시작,y끝,시작)
    rec.append((x,y,y+h,1))
    #x축으로 봤을때 종료점 (x+w,y시작,y끝,종료)
    rec.append((x+w,y,y+h,-1))
    
rec.sort()
area = 0
yList = [0]*10001

for idx in range (len(rec)-1):
    x,y1,y2,flag = rec[idx]
    
    for i in range (y1,y2):
        yList[i] += flag

    ylen = 0
    for y in yList:
        if y != 0:
            ylen += 1
    
    area += (ylen/100)* (rec[idx+1][0]-x)
    
# 단 값이 소수 부분이 없이 정수로 맞아 떨어지는경우
if area-int(area) > 0:
    print(f'{area:0.2f}')
else:
    print(int(area))
            
    
    