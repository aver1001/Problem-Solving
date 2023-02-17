from calendar import c
from dis import dis
from locale import currency
import sys
sys.stdin = open('input.txt', "r")

'''
웜홀은 방향이 있음 
A  => B 도착했을때 시간이 거꾸로 감

도로는 방향이 없음
A <=> B 도착했을떄 시간이 그대로 감

한 지점에서 출발을 해서 원래의 위치로 돌아왔을경우 시간이 줄어들경우가 있을까요?

돌아온다 => 순환한다
순환했을때 순환하는 친구들끼리의 합이 음수일경우 계속돌면 과거로 가는게 가능

순환하는 경우를 찾아서 순환하는 친구딜끼리의 합이 음수인것을 찾아라!

'''


def bf():

    for i in range(N):
        for j in range(2*M+W):
            cur, Next, cost = road[j]

            if dist[Next] > dist[cur] + cost:
                dist[Next] = dist[cur] + cost
                if i == N-1:
                    return True
    print(dist)
    return False


TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    # 지점의 수 N, 도로의 개수 M, 웜홀의 개수 W
    N, M, W = map(int, sys.stdin.readline().rstrip().split(' '))

    road = []
    for _ in range(M):
        # S와 E는 연결된 지점의 번호 T는 도로를 통해 이동하는 시간
        S, E, T = map(int, sys.stdin.readline().rstrip().split(' '))
        road.append([S, E, T])
        road.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().rstrip().split(' '))

        road.append([S, E, -T])

    dist = [sys.maxsize]*(N+1)

    if bf():
        print('YES')
    else:
        print('NO')
