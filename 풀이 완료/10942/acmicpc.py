import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
DP = [[None]*(N) for _ in range (N)]

def printBoard():
    for i in DP:
        print(i)

def isPel(start,end):
    print(start,end)
    if end - start <= 1:
        if numbers[start] == numbers[end]:
            DP[start][end] = True
        else:
            DP[start][end] = False
    else:
        if DP[start][end] == None:
            DP[start][end] = isPel(start+1,end-1) and numbers[start] == numbers[end]
    
    return DP[start][end]

M = int(sys.stdin.readline().rstrip())
for _ in range (M):
    S,E = map(int, sys.stdin.readline().rstrip().split())
    S -= 1
    E -= 1
    print('Start',S,E)
    if isPel(S,E) :
        print(1)
    else:
        print(0)

print(numbers)