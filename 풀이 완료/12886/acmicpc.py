import sys
sys.stdin = open('input.txt', "r")
sys.setrecursionlimit(100000)
A,B,C = map(int, sys.stdin.readline().rstrip().split())

DP = [[False]* 1500 for _ in range (1500)]
def DFS(a : int, b : int , c : int):
    #print(a,b,c)
    
    if DP[a][b]:
        return
    
    if (DP[a][b] == False):
        DP[a][b] = True
        DP[b][a] = True
        
    if a == b == c:
        print(1)
        exit()
    
    
    if (a > b):
        DFS(a-b,b*2,c)
    if (a > c):
        DFS(a-c,b,c*2)
    if (b > c):
        DFS(a,b-c,c*2)
    if (a < b):
        DFS(a*2,b-a,c)
    if (a < c):
        DFS(a*2,b,c-a)
    if (b < c):
        DFS(a,b*2,c-b)
        
            
DFS(A,B,C)
print(0)