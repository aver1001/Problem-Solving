import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
DP = [0]*(N+1)
for idx in range (N):
    day, money = map(int, sys.stdin.readline().rstrip().split())
    DP[idx] = max(DP[idx-1],DP[idx])
    if idx+day < N+1:
        DP[idx+day] = max(DP[idx+day],DP[idx]+money)

DP[N] = max(DP[N-1],DP[N])
print(DP[-1])