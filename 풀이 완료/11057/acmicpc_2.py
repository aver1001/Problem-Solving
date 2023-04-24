import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline())

DP = [-1, 1, 2, 3, 4, 5, 6, 9, 12, 16, 20,27, 36, 48, 64, 81, 108, 144, 192, 256, 324] + [0]*80
for i in range (20,101):
    DP[i] = DP[i-3]*2
print(DP[N])