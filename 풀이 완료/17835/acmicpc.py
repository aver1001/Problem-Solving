import sys
import heapq
sys.stdin = open('input.txt', "r")

N, M, K = map(int, sys.stdin.readline().rstrip().split())

route = {i :{} for i in range (1,N+1)}

for _ in range (M):
    '''
    입력을 받을때 도시를 반대로 받아준다.
    예를들어 A -> B 방향의 도로라면
    B -> A 방향의 도로로 저장한다.
    이 이유는, 우리는 도시에서 면접장으로 이동해야하는데, 모든 도시에서 부터 면접장의 거리를 잰다는것은
    입력 크기가 커서 시간복잡도 상 문제가 발생할 수 있음.
    
    그러므로, 면접장들의 위치를 다엑스트라 초기 힙에 넣어두고 돌릴건데 이때, 도로를 반대로 적용해야
    도시에서 면접장으로 오는길들을 정확하게 찾을 수 있다,
    
    첫번쨰 입력을 그려보고, 3번도시를 확인해보면 이해가 가능할것.
    '''
    v,u,c = map(int, sys.stdin.readline().rstrip().split())    
    if v not in route[u]:
        route[u][v] = c
    else:
        route[u][v] = min(route[u][v], c)

#면접장 위치
targets = list(map(int, sys.stdin.readline().rstrip().split()))
heap = []
#거리 최대값으로 초기화
dis = [sys.maxsize]*(N+1)

#면접장들은 거리를 0으로 초기화 해주고
#힙에다가 다엑스트라 시작지점 넣어준다
for target in targets:
    heapq.heappush(heap,(0,target))
    dis[target] = 0
dis[0] = 0
    
#다엑스트라 진행
while heap:
    #최소 거리인거 뺴주고
    cost,loc = heapq.heappop(heap)
    
    if dis[loc] < cost:
        continue
    
    #이 위치에서 갈수있는 위치들을 확인한다
    for nextLoc, nextCost in route[loc].items():
        costHap = cost+nextCost
        
        #이 거리가 원래 거리보다 가까울경우
        if dis[nextLoc] > costHap:
            #거리 업데이트 해주고
            dis[nextLoc] = costHap
            heapq.heappush(heap,(costHap,nextLoc))
            
maximum = 0
answerIdx = 0
for idx in range (1,N+1):
    if dis[idx] > maximum:
        maximum = dis[idx]
        answerIdx = idx
print(answerIdx,maximum,sep="\n")