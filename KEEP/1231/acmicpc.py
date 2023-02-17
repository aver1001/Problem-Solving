import sys
sys.stdin = open('input.txt', "r")

C,D,M = map(int, sys.stdin.readline().rstrip().split())
costs = []
for _ in range (C):
    costs.append(list(map(int, sys.stdin.readline().rstrip().split())))

def DFS(v,money):
    #print(v,money)
    if v == D-1:
        return money
    
    answer = money
    for idx in range (C):
        cnt = money//costs[idx][v]
        answer = max(answer,costs[idx][v+1]*cnt + money%costs[idx][v])
    return DFS(v+1,answer)
            
print(DFS(0,M))

