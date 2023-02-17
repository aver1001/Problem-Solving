from math import factorial
import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
K = int(sys.stdin.readline().rstrip())

possible = 0
'''
DFS 백트레킹?

'''
print(nums, K)


def DFS(num, isvisited, cnt):
    global possible

    if cnt == N:
        possible += 1
        print(num)
        return

    for idx in range(N):
        if isvisited[idx] == False and (int(str(nums[idx])+num) % K == 0 or (len(str(nums[idx])+num) > len(str(K)))):
            isvisited[idx] = True
            DFS(str(nums[idx])+num, isvisited, cnt+1)
            isvisited[idx] = False


DFS('', [False]*N, 0)
print(possible/factorial(N))

# 안되는데 되는건 가능?
