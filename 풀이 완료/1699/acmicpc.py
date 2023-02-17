import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())


DP = [i for i in range (N+1)]

for i in range (2,N+1):
    for j in range (i+1):
        if j**2 > i:
            break
        DP[i] = min(DP[i],DP[i-j**2]+1) 
print(DP[-1])
