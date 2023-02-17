import sys
from bisect import bisect_left, bisect_right
sys.stdin = open('input.txt', "r")

N = int(input())

commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))
stack = [commend[0]]
for idx in range(1, N):
    if stack[-1] <= commend[idx]:
        stack.append(commend[idx])
    else:
        stack[bisect_left(stack, commend[idx])] = commend[idx]

print(len(stack))
