import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

board = [[0,0] for _ in range (10001)]

for _ in range (N):
    x,y,w,h = map(float,sys.stdin.readline().rstrip().split())
    x = int(10*x)
    y = int(10*y)
    w = int(10*w)
    h = int(10*h)
    


