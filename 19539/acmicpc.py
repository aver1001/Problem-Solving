import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
trees = map(int, sys.stdin.readline().rstrip().split(' '))
two = 0
one = 0


for tree in trees:
    two += tree // 2
    one += tree % 2

if sum(trees) % 3 == 0 and two >= one and (two-one) % 3 == 0:
    print('YES')
else:
    print('NO')
