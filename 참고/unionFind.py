import sys
sys.stdin = open('input.txt', "r")
v = int(input())
N = int(input())
parent = [0] * (v + 1)  # 부모 테이블 초기화하기


def find(x):
    # 만약 자기자신이 아니라면 == 루트노드가 아니라면
    if parent[x] != x:
        # 가리키는 노드 찾아가서 업데이트 해준다
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    # 양쪽다 부모를 찾아준뒤
    a = find(a)
    b = find(b)

    # 작은쪽으로 합쳐준다
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        # 자기 자신을 바라도록 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(N):
    a, b, c = map(int, input().split())
    union(a, b)
