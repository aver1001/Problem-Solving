from dis import dis
import sys
sys.stdin = open('input.txt', "r")

V = int(sys.stdin.readline().rstrip())
table = {}
for _ in range(V):
    Vlist = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    table[Vlist[0]] = {}
    for idx in range(1, len(Vlist)-1, 2):
        table[Vlist[0]][Vlist[idx]] = Vlist[idx+1]

print(table)

# 트리 ==> 서로 다 연결되어있음, 순환되지 않음.
answer = 0
isVisited = [False]*(V+1)


def DFS(node, cost):
    global answer
    # 방문노드 체크
    isVisited[node] = True

    # 자식노드들의 거리를 계산할 distance 배열 선언
    distance = []
    test = []

    # 자식 노드들 방문하면서
    for nextNode, nextCost in table[node].items():
        # 방문하지 않았을 경우만 확인 (자식노드)
        if isVisited[nextNode] == True:
            continue

        # 거리를 저장해줌
        test.append(nextNode)
        distance.append(DFS(nextNode, cost+nextCost))
    print(node, distance)
    # 자식 노드가 0개일경우 루트찾기 불가능,
    if len(distance) == 0:
        print(cost)
        return 0
    # 자식 노드가 1개일경우 여기서 루트를 찾을 필요는 없음.
    elif len(distance) == 1:
        answer = max(answer, cost+distance[0])
        return cost
    else:
        # 루트의 최대값을 업데이트 해줌
        answer = max(answer, distance[-1], distance[-2])
        return cost + distance[-1]


DFS(1, 0)
print(answer)
