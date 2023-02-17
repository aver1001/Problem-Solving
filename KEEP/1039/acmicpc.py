import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split())
N = str(N)
target = []
for idx in range(len(N)):
    target.append(int(N[idx]))
N = target.copy()
target.sort(reverse=True)

if len(N) == 1:
    print(-1)
    exit()

if len(N) == 2 and 0 in N:
    print(-1)
    exit()
print(N)
for _ in range(K):

    for idx in range(len(N)):

        if N[idx] == target[idx]:
            continue
        
        cnt = N.count(target[idx])

        for i in range(len(N)):
            if N[i] == target[idx]:
                cnt -= 1
            if cnt == 0:
                break
        N[idx], N[i] = N[i], N[idx]
        break
    else:
        N[-1], N[-2] = N[-2], N[-1]
    print(N)
for i in N:
    print(i, end='')

