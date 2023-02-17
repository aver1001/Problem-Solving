import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
limit = list(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())
weight = list(map(int, sys.stdin.readline().rstrip().split(' ')))


if max(weight) > max(limit):
    print(-1)
    exit()

weight.sort(reverse=True)
limit.sort(reverse=True)

cnt = 0
while weight:
    for l in limit:
        for idx in range(len(weight)):
            if weight[idx] <= l:
                break
        else:
            break
        weight.pop(idx)
    cnt += 1

print(cnt)
