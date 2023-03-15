import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline())

def solution(node,cost):
    
    isLeaf = True
    hap = 0
    for nextNode,nextCost in table[node].items():
        if isVisited[nextNode] == False:
            isLeaf = False
            isVisited[nextNode] = True
            hap += solution(nextNode,nextCost)

    if isLeaf:
        return cost
    else:
        if node == 1:
            return hap
        else:
            return min(hap,cost)

for test_case in range (T):
    N,M = map(int,sys.stdin.readline().split())
    table = {i:{} for i in range(1,N+1) }
    for _ in range (M):
        u,v,cost = map(int,sys.stdin.readline().split())
        table[u][v] = cost
        table[v][u] = cost
        
    isVisited = [False]*(N+1)
    isVisited[1] = True
    
    print(solution(1,0))
