import sys
from collections import deque

sys.stdin = open('input.txt', "r")

def dfs(loc:int,v:int):
    state = True
    #나는 v로 설정해주고
    Check[loc] = v
    
    #인접한것들을 방문하면서
    for nextLoc in table[loc]:
        #방문하지 않았다면
        if Check[nextLoc] == 0:
            #DFS진행
            state &= dfs(nextLoc,v+1)
        #이미 방문했다면
        else:
            #만약 나와 그친구의 위치가 서로 같다면 이는 이분그래프가 만들어질수 없다는 것을 의미
            if Check[nextLoc]%2 == v%2:
                return False
    return state

def solution():
    for idx in range (1,V+1):
        if Check[idx] == 0:
            if dfs(idx,1) == False:
                return False
    return True

K = int (sys.stdin.readline().rstrip())
for _ in range (K):
    #정점V(1~V) 간선
    V,E = map(int, sys.stdin.readline().rstrip().split())
    table = {i:set() for i in range (1,V+1)}
    #방문확인 + 분리 확인
    Check = [0]*(V+1)
    for _ in range (E):
        u,v = map(int, sys.stdin.readline().rstrip().split())
        table[u].add(v)
        table[v].add(u)
    
    if solution():
        print("YES")
    else:
        print("NO")


