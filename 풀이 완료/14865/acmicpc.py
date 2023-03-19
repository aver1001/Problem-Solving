import sys
from collections import deque
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline())

temp = []
beforeY = 0
beforeX = 0
pos = []
zero = set()
for _ in range (N):
    nowX,nowY = map(int, sys.stdin.readline().rstrip().split())
    
    if (beforeY * nowY) < 0:
        temp.append((nowY,nowX))
        zero.add(nowX)
        
            
    beforeY = nowY

table = {}

while (temp):
    num1 = temp.pop()
    num2 = temp.pop()
print(temp)
print(sorted(zero))
