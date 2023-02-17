import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

commend = []
for _ in range(M):
    a, b, cost = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    commend.append([cost, a, b])
heapq.heapify(commend)

table = [i for i in range(N)]
answer = 0


def findParent(a):
    # 부모노드
    if table[a] == a:
        return a

    p = findParent(table[a])
    table[a] = p
    return table[a]


def UnionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a > b:
        table[a] = b
    else:
        table[b] = a


while commend:

    cost, a, b = heapq.heappop(commend)
    a -= 1
    b -= 1

    # 사이클이 없다면 연결 후 업데이트
    if findParent(a) != findParent(b):
        print(a, b)
        answer += cost
        UnionParent(a, b)
        print(table)
    # 사이클이 있다면 패스
    else:
        continue

print(answer)
