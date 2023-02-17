import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
answer = [0]*(N+1)

cnt = 1
answer[1] = cnt

for idx in range(2, N+1):

    if answer[idx] == 0:
        cnt += 1
        for idx2 in range(idx, N+1, idx):
            answer[idx2] = cnt
print(cnt)
print(*answer[1:])
