import sys
import math
from itertools import combinations
sys.stdin = open('input.txt', "r")

for _ in range (int(sys.stdin.readline().rstrip())):
    vector = []
    for _ in range (int(sys.stdin.readline().rstrip())):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        vector.append((y,x))
    N = len(vector)
    answer = sys.maxsize
    combi = list(combinations(range(N),N//2))
    for add in combi[:len(combi)//2] :
    
        y = 0
        x = 0
        
        for idx in range (N):
            if idx in add:
                x += vector[idx][0]
                y += vector[idx][1]
            else:
                x -= vector[idx][0]
                y -= vector[idx][1]
                
        answer = min(answer,math.sqrt(x**2 + y**2))
    print(answer)
    
                
    