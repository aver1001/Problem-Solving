import sys
sys.stdin = open('input.txt', "r")


N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())


def numCnt(target):

    temp = 0
    for y in range(1, N+1):
        temp += min(N, target//y)

    return temp


lt, rt = 0, K

while lt <= rt:

    mid = (lt+rt) // 2

    temp = numCnt(mid)

    if temp >= K:
        answer = mid
        rt = mid-1
    else:
        lt = mid+1

print(answer)
