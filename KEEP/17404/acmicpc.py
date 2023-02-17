import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
INF = 1000*N
costs = []
for _ in range (N):
    
    R, G, B = map(int, sys.stdin.readline().rstrip().split())
    costs.append((R,G,B))
    
answer = INF
for idx in range (3):
    
    DP = [[0,0,0] for _ in range (N)]
    DP[0] = [INF,INF,INF]
    DP[0][idx] = costs[0][idx]
    
    for n in range (1,N):
        
        DP[n][0] = min(DP[n-1][1],DP[n-1][2]) + costs[n][0]
        DP[n][1] = min(DP[n-1][0],DP[n-1][2]) + costs[n][1]
        DP[n][2] = min(DP[n-1][0],DP[n-1][1]) + costs[n][2]

    DP[-1][idx] = INF
    answer = min(*DP[-1],answer)
print(answer)