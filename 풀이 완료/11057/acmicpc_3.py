import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline())
DP = [0]*101
for i in range (7):
    DP[i]= i

for i in range (7,101):
    DP[i] = max(DP[i-3]*2,DP[i-4]*3,DP[i-5]*4)
print(DP[N])