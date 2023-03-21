import sys
sys.stdin = open('input.txt', "r")

def dfs(N,L,R):
    
    if L < 0 or R < 0:
        return 0
    
    if N == 0:
        if L == R == 0:
            return 1
        return 0
    
    if DP[N][L][R] != -1:
        return DP[N][L][R]
    
    #왼쪽끝 설치
    DP[N][L][R] = dfs(N-1,L-1,R) + dfs(N-1,L,R-1) + (N-1)*dfs(N-1,L,R)
    DP[N][L][R] %= 1_000_000_007
    return DP[N][L][R]
    

N,L,R = map(int, sys.stdin.readline().rstrip().split())
DP = [[[-1]*(R) for _ in range (L)] for _ in range (N)]
print(dfs(N-1,L-1,R-1))