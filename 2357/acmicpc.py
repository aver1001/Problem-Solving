import sys
import math
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(N):
    board.append(int(sys.stdin.readline().rstrip()))

Maxtree = [0] * 2 ** math.ceil(math.log2(N)+1)
Mintree = [0] * 2 ** math.ceil(math.log2(N)+1)


def MaxStreeInit(left, right, node, tree):

    # 세그먼트 트리를 초기화 해준다
    if left == right:
        # 마지막 리프 노드에 도착햇을경우 배열의 자신의 위치의 값을 넣어준뒤 리턴해준다
        tree[node] = board[left]
        return tree[node]
    else:
        # 마지막 리프가 아닐경우 자신의 노드는 왼쪽 오른쪽 노드를 불러온뒤 더해준값을 넣어준다
        mid = (left+right) // 2
        tree[node] = max(MaxStreeInit(left, mid, node*2, tree),
                         MaxStreeInit(mid+1, right, node*2 + 1, tree))
        return tree[node]


def MinStreeInit(left, right, node, tree):

    # 세그먼트 트리를 초기화 해준다
    if left == right:
        # 마지막 리프 노드에 도착햇을경우 배열의 자신의 위치의 값을 넣어준뒤 리턴해준다
        tree[node] = board[left]
        return tree[node]
    else:
        # 마지막 리프가 아닐경우 자신의 노드는 왼쪽 오른쪽 노드를 불러온뒤 더해준값을 넣어준다
        mid = (left+right) // 2
        tree[node] = min(MinStreeInit(left, mid, node*2, tree),
                         MinStreeInit(mid+1, right, node*2 + 1, tree))
        return tree[node]


def StreeMax(left, right, node, tree, targetLeft, targetRight):

    # 우리가 찾으려는 범위 안에 오른쪽 왼쪽이 둘다 들어올경우
    if left >= targetLeft and right <= targetRight:
        # 우리가 위치한 노드의 값을 리턴
        return tree[node]

    # 우리가 찾으려넌 범위 밖에 오른쪽 왼쪽이 둘다 넘어갈 경우
    elif left <= targetRight and right >= targetLeft:
        # 왼쪽 오른쪽 탐색
        mid = (left+right) // 2
        return max(StreeMax(left, mid, node*2, tree, targetLeft, targetRight), StreeMax(mid+1, right, node*2 + 1, tree, targetLeft, targetRight))

    return 0


def StreeMin(left, right, node, tree, targetLeft, targetRight):

    # 우리가 찾으려는 범위 안에 오른쪽 왼쪽이 둘다 들어올경우
    if left >= targetLeft and right <= targetRight:
        # 우리가 위치한 노드의 값을 리턴
        return tree[node]

    # 우리가 찾으려넌 범위 밖에 오른쪽 왼쪽이 둘다 넘어갈 경우
    elif left <= targetRight and right >= targetLeft:
        # 왼쪽 오른쪽 탐색
        mid = (left+right) // 2
        return min(StreeMin(left, mid, node*2, tree, targetLeft, targetRight), StreeMin(mid+1, right, node*2 + 1, tree, targetLeft, targetRight))

    return sys.maxsize


MaxStreeInit(0, N-1, 1, Maxtree)
MinStreeInit(0, N-1, 1, Mintree)


for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(StreeMin(0, N-1, 1, Mintree, a-1, b-1),
          StreeMax(0, N-1, 1, Maxtree, a-1, b-1))
