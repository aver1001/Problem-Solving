import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input.txt', "r")
MAX = 400000

table =[
    [0,2,2,2,2],
    [0,1,3,4,3],
    [0,3,1,3,4],
    [0,4,3,1,3],
    [0,3,4,3,1]
]

commend = list(map(int, sys.stdin.readline().rstrip().split()))

DP = [[[-1]* 5 for _ in range (5)] for _ in range (len(commend)-1)]

        
def DFS(v,left,right):
    
    '''
    오른쪽발을 움직였을 경우 cost와
    왼쪽발을 움직였을 경우의 cost를 구해서
    그중 더 작은값을 택한다.
    '''
    if commend[v] == 0:
        return 0
    
    if DP[v][left][right] != -1:
        return DP[v][left][right]
    
    
    
    DP[v][left][right] = min(DFS(v+1,commend[v],right)+table[left][commend[v]],DFS(v+1,left,commend[v])+table[right][commend[v]])
    return DP[v][left][right]
print(DFS(0,0,0))

# for i in DP:
#     for j in i:
#         print(j)
#     print()



