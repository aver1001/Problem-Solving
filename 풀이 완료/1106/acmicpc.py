import sys
sys.stdin = open('input.txt', "r")

C,N = map(int, sys.stdin.readline().rstrip().split())
DP = [sys.maxsize]*(C+100)
DP[0] = 0
for _ in range (N):
    cost,people = map(int, sys.stdin.readline().rstrip().split())
    DP[people] = min(cost,DP[people])
    for idx in range (people,C+100):
        DP[idx] = min(DP[idx],DP[idx-people]+cost)
print(min(DP[C:]))
