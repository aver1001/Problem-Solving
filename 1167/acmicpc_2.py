import sys
sys.stdin = open('input.txt', "r")

V = int(sys.stdin.readline().rstrip())
table = {}
for _ in range(V):
    Vlist = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    table[Vlist[0]] = {}
    for idx in range(1, len(Vlist)-1, 2):
        table[Vlist[0]][Vlist[idx]] = Vlist[idx+1]


# 트리 ==> 서로 다 연결되어있음, 순환되지 않음.
answer = 0
isVisited = [False]*(V+1)


def DFS(node):
    global answer
    # 방문노드 체크
    isVisited[node] = True

    # 자식노드들의 거리를 계산할 distance 배열 선언
    distance = []

    # 자식 노드들 방문하면서
    for nextNode, nextCost in table[node].items():
        # 방문하지 않았을 경우만 확인 (자식노드)
        if isVisited[nextNode] == True:
            continue

        # 거리를 저장해줌
        distance.append(DFS(nextNode)+nextCost)
    distance.sort()

    # 자식 노드가 0개일경우 루트찾기 불가능,
    if len(distance) == 0:
        return 0
    # 자식 노드가 1개일경우
    elif len(distance) == 1:
        answer = max(answer, distance[0])
        return distance[0]
    else:
        # 루트의 최대값을 업데이트 해줌
        answer = max(answer, distance[-1]+distance[-2])
        return distance[-1]


DFS(1)
print(answer)
