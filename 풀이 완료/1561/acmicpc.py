import sys
sys.stdin = open('input.txt', "r")

# N 아이들 수
# M 놀이기구 수
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

lt, rt = 0, 60000000000
while lt <= rt:

    mid = (lt+rt) // 2
    answer = M
    for c in commend:
        answer += mid // c

    if answer >= N:
        t = mid
        rt = mid-1
    else:
        lt = mid+1

print(t)
if mid == 0:
    print(N)
else:

    cnt = M
    for c in commend:
        cnt += (t-1) // c

    for idx in range(M):
        if commend[idx] % t == 0:
            cnt += 1

        if cnt == N:
            print(idx)
