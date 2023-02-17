import sys
sys.stdin = open('input.txt', "r")

def findLine(x1,y1,x2,y2):
    if x1 == x2:
        a = 0
    else:
        a = (y1-y2)/(x1-x2)
    b = y1 - a*x1
    return a,b

def isCoross(a1,b1,a2,b2,x11,y11,x12,y12,x21,y21,x22,y22):
    
    if a1-a2 == 0:
        #기울기가 같을경우
        if b1 == b2 :
            return 1
        
        return 0
    else:
        x = (b2-b1)/(a1-a2)
        y = a1*x + b1
        if min(x11,x12)<= x <= max(x11,x12) and min(y11,y12) <= y <= max(y11,y12) and min(x21,x22)<= x <= max(x21,x22) and min(y21,y22) <= y <= max(y21,y22):
            return 1
        else:
            return 0 


x11,y11,x12,y12 = map(int, sys.stdin.readline().rstrip().split())
x21,y21,x22,y22 = map(int, sys.stdin.readline().rstrip().split())

if min(x11,x12)<= x21 <= max(x11,x12) or min(x11,x12)<= x22 <= max(x11,x12) or min(x21,x22)<= x11 <= max(x21,x22) or min(x21,x22)<= x12 <= max(x21,x22):
    if min(y11,y12)<= y21 <= max(y11,y12) or min(y11,y12)<= y22 <= max(y11,y12) or min(y21,y22)<=y11 <= max(y21,y22) or min(y21,y22)<= y12 <= max(y21,y22):
        a1,b1 = findLine(x11,y11,x12,y12)
        a2,b2 = findLine(x21,y21,x22,y22)
        print(isCoross(a1,b1,a2,b2,x11,y11,x12,y12,x21,y21,x22,y22))
        exit()
print(0)


