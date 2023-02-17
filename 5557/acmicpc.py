import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))
global answer
answer = 0
DP = [[0]*21 for _ in range(N-1)]

for idx in range(len(commend)-1):
    # 첫번쨰 인덱스의 경우 1 넣어준다
    if idx == 0:
        DP[idx][commend[idx]] = 1
        continue

    # commend[idx] 수
    for idx2 in range(21):
        if 0 <= idx2 + commend[idx] <= 20:
            DP[idx][idx2 + commend[idx]] += DP[idx-1][idx2]
        if 0 <= idx2 - commend[idx] <= 20:
            DP[idx][idx2 - commend[idx]] += DP[idx-1][idx2]


print(DP[-1][commend[-1]])
