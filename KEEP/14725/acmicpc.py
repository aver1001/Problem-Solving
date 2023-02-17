import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

route = dict()

for _ in range(N):
    commend = sys.stdin.readline().rstrip().split(' ')
    tempRoute = route

    for idx in range(1, int(commend[0])+1):

        if commend[idx] not in tempRoute:
            tempRoute[commend[idx]] = {}

        tempRoute = tempRoute[commend[idx]]


def DFS(tree, v):
    # 키값 가져옴
    key = list(tree.keys())
    # 키값 사전순으로 정렬해줌
    key.sort()

    for k in key:
        print('--'*v, k, sep='')
        DFS(tree[k], v+1)


DFS(route, 0)
