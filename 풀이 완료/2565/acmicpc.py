import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

N = int(input())
board= []
for _ in range (N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    board.append([A,B])
board.sort()

stack = []

for _,B in board:
    location = bisect_left(stack,B)
    if location >= len(stack):
        stack.append(B)
    else:
        stack[location] = B
    
print(N-len(stack))