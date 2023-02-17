import sys
import heapq
sys.stdin = open('input.txt', "r")
'''
서강 나라의 대통령은 최근 개발이 완료된 YNY 프로젝트를 진행한다.

발전소는 이미 특정 도시에 건설되어 있고, 따라서 추가적으로 드는 비용은 케이블을 설치할 때 드는 비용이 전부임.
케이블 설치 비용이 굉장히 크므로 이를 최소하해서 모든 도시에 전기를 공급하는 것이 목표

N개의 도시가 있고, M개의 두 도시를 연결하는 케이블의 정보,K개의 발전소의 위치가 주어지면
케이블 설치비용을 최소로 사용해서 모든 도시에 전기가 공급될 수 있도록 해야함.

중요한점은 어느 한 도시가 두 개의 발전소에서 전기를 공급받으면 낭비가 되므로
케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다.

'''

N, M, K = map(int, sys.stdin.readline().rstrip().split())
elect = set(map(int, sys.stdin.readline().rstrip().split()))
cost = {}
for _ in range(M):
    # u도시와 v도시를 연결할때 w비용
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    if u in cost:
        cost[u][v] = w
    else:
        cost[u] = {}
        cost[u][v] = w

    if v in cost:
        cost[v][u] = w
    else:
        cost[v] = {}
        cost[v][u] = w

# 발전소에 연결되어 있는 친구들을 먼저 넣어주자.
city = []
answer = 0
for e in elect:
    for nextLoc, value in cost[e].items():
        heapq.heappush(city, (value, nextLoc))

while city:
    value, Loc = heapq.heappop(city)
    # 이미 전기가 들어간 도시일 경우 무시한다.

    if Loc in elect:
        continue

    # 연결시키고 비용을 추가한다.
    elect.add(Loc)
    answer += value

    # 연결시킨 도시에서 연결할 수 있는 도시들을 heap에 추가해준다.
    for nextLoc, value in cost[Loc].items():
        # 연결되지 않은 도시일경우만 넣어준다.
        if nextLoc not in elect:
            heapq.heappush(city, (value, nextLoc))

print(answer)
