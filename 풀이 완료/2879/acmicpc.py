import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
start = list(map(int, sys.stdin.readline().rstrip().split()))
end = list(map(int, sys.stdin.readline().rstrip().split()))

target = []
for s,e in zip(start,end):
    target.append(e-s)

print(target)

queue = deque([])

before = 0
for t in target:
    if t