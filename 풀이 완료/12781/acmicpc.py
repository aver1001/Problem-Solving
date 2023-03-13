import sys
sys.stdin = open('input.txt', "r")

x1,y1,x2,y2,x3,y3,x4,y4 = map(int, sys.stdin.readline().rstrip().split())


def ccw(x1,y1,x2,y2,x3,y3):
    '''
    x1  x2  x3  x1
    y1  y2  y3  y1
    '''
    return x1*y2 + x2*y3 + x3*y1 -(y1*x2 + y2*x3 + y3 * x1)

if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) < 0:
    
    print(1)
else:
    print(0)