import sys
import time
from collections import deque

N = 7
Flow = [[0]*N for _ in range (N)]   #각각의 유량을 저장할 배열
currentFlow = [[0]*N for _ in range (N)] #현재 노드들끼리의 유량의 정보를 저장할 배열
route = [set() for _ in range (N)]  #연결되어있는 노드들의 정보를 저장할 배열
def MaxFlow(start,end):
    answer = 0
    while True:
        #방문체크, 경로를 저장할 배열 초기화
        root = [-1]*N
        #시작부터 BFS 진행
        queue = deque([start])
        while queue:
            now = queue.popleft()
            for next in route[now]:
                #유량이 움직일수 있다면 && 방문하지 않았다면
                if (Flow[now][next] - currentFlow[now][next] > 0 and root[next] == -1):
                    #방문 표시 해주고
                    root[next] = now
                    #큐에 추가 해준다
                    queue.append(next)
                    #만약 마지막까지 왔다면 break
                    if (next == end):
                        break
        #더이상 마지막까지 도착할 수 없다면 break
        if root[end] == -1:
            break
        now = end   #도착지에서 시작해서 역주행하기위해 변수 선언
        flow = sys.maxsize # 유량의 최솟값을 찾기위해 최대값으로 초기화
        while True:
            next = root[now]    #다음위치를 now의 부모로 잡고
            if now == start:    #기저조건
                break
            flow = min (flow,Flow[next][now] - currentFlow[next][now]) #최솟값을 찾음
            now = next          #지금 위치를 다음위치로 변경
            
        answer += flow  #유량을 더해줌
        
        now = end
        while True:
            next = root[now]
            if now == start:
                break
            currentFlow[now][next] -= flow
            currentFlow[next][now] += flow
            now = next
            
    print(answer)

route[1].add(2)
route[2].add(1)
Flow[1][2] += 12

route[1].add(4)
route[4].add(1)
Flow[1][4] += 11

route[2].add(3)
route[3].add(2)
Flow[2][3] += 6

route[2].add(4)
route[4].add(2)
Flow[2][4] += 3

route[2].add(5)
route[5].add(2)
Flow[2][5] += 5

route[2].add(6)
route[6].add(2)
Flow[2][6] += 9

route[3].add(6)
route[6].add(3)
Flow[3][6] += 8

route[4].add(5)
route[5].add(4)
Flow[4][5] += 9

route[5].add(3)
route[3].add(5)
Flow[5][3] += 3

route[5].add(6)
route[6].add(5)
Flow[5][6] += 4

print(route)
MaxFlow(1,6)