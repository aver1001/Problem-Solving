import sys
sys.stdin = open('input.txt', "r")
'''
1. 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 합니다.
2. 같은 그림을 두 번 이상 사는 것은 불가능합니다.
'''
N = int(sys.stdin.readline().rstrip())
cost = [[] for i in range(N)]

for idx in range(N):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(N):
        if idx == j:
            continue
        #[가격, 다음위치]
        cost[idx].append([int(temp[j]), j])


global answer
answer = 1
# 가격, 전의 위치, 지금위치 안에다가 횟수
DP = [[[0]*10 for _ in range(N)] for _ in range(N)]


def DFS(nowLoc, nowCost, cnt, visited):
    global answer
    answer = max(answer, cnt)
    # 초기 설정값
    # nowLoc = 0
    # nowCost = 0
    # cnt = 1
    # visited = [True, False, False ... False]

    for nextCost, nextLoc in cost[nowLoc]:
        # 다음 가격이 내 가격보다 같거나 비싸고 AND 방문하지 않았을 경우
        if nextCost < nowCost:
            continue

        if visited[nextLoc] == False and DP[nowLoc][nextLoc][nowCost] < cnt + 1:
            DP[nowLoc][nextLoc][nowCost] = cnt+1
            visited[nextLoc] = True
            DFS(nextLoc, nextCost, cnt+1, visited)
            visited[nextLoc] = False


visited = [False]*N
visited[0] = True
DFS(0, 0, 1, visited)
print(answer)
