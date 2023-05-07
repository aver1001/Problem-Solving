import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

N,L,R,X = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

answer  = 0
for i in range (2,N+1):
    for c in combinations(numbers,i):
        hap = sum(c)
        upper = max(c)
        lower = min(c)
        
        if L <= hap <= R and upper-lower >= X:
            answer += 1
print(answer)