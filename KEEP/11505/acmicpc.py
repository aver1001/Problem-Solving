import math
import sys
sys.stdin = open('input.txt', "r")

N, M, K = map(int, sys.stdin.readline().rstrip().split())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline().rstrip()))
numN = len(num)
tree = [0] * 2 ** math.ceil(math.log2(numN)+1)


def StreeInit(left, right, node):
    # 세그먼트 트리를 초기화 해준다
    if left == right:
        # 마지막 리프 노드에 도착햇을경우 배열의 자신의 위치의 값을 넣어준뒤 리턴해준다
        tree[node] = num[left]
        return tree[node]
    else:
        # 마지막 리프가 아닐경우 자신의 노드는 왼쪽 오른쪽 노드를 불러온뒤 더해준값을 넣어준다
        mid = (left+right) // 2
        tree[node] = StreeInit(left, mid, node*2) * \
            StreeInit(mid+1, right, node*2 + 1) % 1_000_000_007
        return tree[node]


def StreeUpadate(left, right, node, idx, value):
    # 세그먼트 트리를 업데이트 해준다
    if left == right == idx:
        # 우리가 찾는 리프노드에 도착햇을경우 값을 변경해준뒤 리턴해준다
        tree[node] = value
        return tree[node]

    if idx < left or right < idx:
        # 우리가 찾는 범위 밖으로 벗어날경우 지금노드를 리턴해준다
        return tree[node]
    else:
        # 우리가 찾는 범위 속 이지만 우리가 찾는 리프노드가 아닐경우
        # 왼쪽 오른쪽 노드를 불러와준뒤 자신의 값을 업데이트 해준다
        mid = (left+right) // 2
        tree[node] = StreeUpadate(
            left, mid, node*2, idx, value) * StreeUpadate(mid+1, right, node*2 + 1, idx, value) % 1_000_000_007
        return tree[node]


def StreeHap(left, right, node, targetLeft, targetRight):

    # 우리가 찾으려는 범위 안에 오른쪽 왼쪽이 둘다 들어올경우
    if left >= targetLeft and right <= targetRight:
        # 우리가 위치한 노드의 값을 리턴
        return tree[node]

    # 우리가 찾으려넌 범위 밖에 오른쪽 왼쪽이 둘다 넘어갈 경우
    elif left <= targetRight and right >= targetLeft:
        # 왼쪽 오른쪽 탐색
        mid = (left+right) // 2
        return StreeHap(left, mid, node*2, targetLeft, targetRight)*StreeHap(mid+1, right, node*2 + 1, targetLeft, targetRight) % 1_000_000_007

    return 1


StreeInit(0, numN-1, 1)
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        # 값 변환 b번째 수를 c로 변경
        StreeUpadate(0, numN-1, 1, b-1, c)
    else:
        # 곱 출력 b부터 c까지의 곱
        print(StreeHap(0, numN-1, 1, b-1, c-1))


# StreeUpadate(0, numN-1, 1, 1, 5)
# print(tree)
