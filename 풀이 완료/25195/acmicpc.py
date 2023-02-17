import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(N)
table = {i :set() for i in range (1,N+1)}
for _ in range (M):
    # u -> v
    u,v = map(int, sys.stdin.readline().rstrip().split())
    table[u].add(v)
S = int(sys.stdin.readline().rstrip())
sSet = set(map(int, sys.stdin.readline().rstrip().split()))

def DFS(Node:int) -> bool:
    if Node in sSet:
        return False
    if len(table[Node]) == 0 :
        return True
    
    state = False
    for nextNode in table[Node]:
        state = state | DFS(nextNode)
    
    return state

isyes = DFS(1)
if isyes:
    print("yes")
else:
    print("Yes")