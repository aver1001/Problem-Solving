import sys
from collections import deque
sys.stdin = open('input.txt', "r")

# K아파트 단지의 개수
N, K = map(int, sys.stdin.readline().rstrip().split(' '))

route = {i: {'leaf': set(), 'root': None} for i in range(1, N+1)}
temp = [[]for _ in range(N+1)]
for _ in range(N-1):
    A, B, cost = map(int, sys.stdin.readline().rstrip().split(' '))
    temp[A].append(B)
    temp[B].append(A)

# root 선택
queue = deque([1])
isVisited = [False]*(N+1)
isVisited[1] = True
while queue:
    Loc = queue.popleft()

    for idx in temp[Loc]:
        if isVisited[idx] == False:
            route[Loc]['leaf'].add(idx)
            route[idx]['root'] = Loc
            isVisited[idx] = True
            queue.append(idx)


dangiCnt = [0]*(N+1)
dangis = set(map(int, sys.stdin.readline().rstrip().split(' ')))


def DFS(Loc):

    cnt = 0

    for i in route[Loc]['leaf']:
        cnt += DFS(i)

    if Loc in dangis:
        cnt += 1

    dangiCnt[Loc] = cnt
    return cnt


DFS(1)

answer = set()
for idx in range(1, N+1):

    if idx in answer:
        continue

    if idx in dangis:
        answer.add(idx)
        continue

    if dangiCnt[idx] == 0:
        continue

    cnt = 0
    for leaf in route[idx]['leaf']:
        if dangiCnt[leaf] > 0:
            cnt += 1

        if cnt == 2:
            answer.add(idx)
            break

    else:
        if cnt == 0:
            pass
        if cnt == 1:
            # 내 위에 단지가 있나요
            if dangiCnt[1] > dangiCnt[idx]:
                answer.add(idx)

print(answer)
print(len(answer))
'''
d(6,5)

5 자리는 아파트 단지

김씨는 1~9에서 디조트 카페 만듬


입력 마지막에 아파트 단지 알려줌

아파트 단지 = 카페를 만들 수 있음

1~9 순회하면서
1에서 가장 가까운 아파트 단지를  찾음
d(1,2) = 8

디저트카페 지을 위치에서 가장 가까운 아파트 단지까지의 거리를 구해

이 거리가 다른 나머지 모든 위치보다 작아야 굿 플레이스

리턴이 굿플레이스의 개수

'''
