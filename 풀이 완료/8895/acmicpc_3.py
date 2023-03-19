import sys
sys.stdin = open('input.txt', "r")

def dfs(n,l,r):
    if l < 0 or r < 0:
        return 0
    
    if n == 0:
        if l == 0 and r == 0:
            return 1
        return 0
    
    if DP[n][l][r] != -1:
        return DP[n][l][r]
    
    #왼쪽설치
    DP[n][l][r] = dfs(n-1,l-1,r) + dfs(n-1,l,r-1) + (n-1) * dfs(n-1,l,r)
    
    return DP[n][l][r]

T = int(sys.stdin.readline().rstrip())
for test_case in range (T):
    
    N, L, R = map(int, sys.stdin.readline().rstrip().split())
    DP = [[[-1]*(R+1) for _ in range (L+1)]for _ in range (N+1)]
    print(dfs(N-1,L-1,R-1))
