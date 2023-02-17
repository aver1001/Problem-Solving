import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range (N):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    numbers.append([A,B])

DP = [[sys.maxsize]*(N)for _ in range (N)]


def DFS(left,right):
    if right-left == 1:
        DP[left][right] = numbers[left][0]*numbers[left][1]*numbers[right][1]
        
    elif left == right:
        DP[left][right] = 0

    elif DP[left][right] == sys.maxsize:
        for mid in range (left,right):
            # print(left,right,'||',mid)
            DP[left][right] = min(DP[left][right],DFS(left,mid) + DFS(mid+1,right)+ numbers[left][0]*numbers[mid][1]*numbers[right][1])
            # print(DP[left][right])
    return DP[left][right]
        

print(DFS(0,N-1))
