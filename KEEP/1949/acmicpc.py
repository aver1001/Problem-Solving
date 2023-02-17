import sys
sys.stdin = open('input.txt', "r")

'''
1~N개의 마을이 있다.
이 나라는 트리구조로 이루어져 있다.
마을과 마을 사이를 직접 잇는 N-1개의 길이 있다. 방향성은 없다
두마을을 직접 잇는 길이 있을 때 두 마을이 인접해 있다고 한다.

다음 세가지 조건을 만족하면서 N개의 마을 중 몇개의 마을을 우수마을로 선정하려고 한다.

1. 우수마을로 선전된 마을 주민 수의 총 합을 최대로 해야한다.
2. 마을사이의 충돌을 방지하기 위해 두 마을이 인접해 있으면 두 마을을 모두 우수마을로 선정할수는 없다
    즉 우수마을끼리는 서로 인접해 있을 수 없음.
3. 선정되지 못한 마을에 경각심을 일으키기 위해 우수마을로 선정되지 못한 마을은 적어도 하나의 우수마을과는 이접해 있어야 한다.

각 마을 주민 수와 마을 사이의 길에 대한 정보가 주어졌을때, 주어진 조건을 만족하도록 '우수 마을' 을 선정하는 프로그램을 작성하라.

'''
N = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split(' ')))
table = {}
isVisited = [False]*(N+1)
isVisited[1] = True
DP = [[0, 0] for _ in range(N+1)]  # ON OFF
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    if a in table:
        table[a].add(b)
    else:
        table[a] = set()
        table[a].add(b)

    if b in table:
        table[b].add(a)
    else:
        table[b] = set()
        table[b].add(a)

def DFS(node):

    # 방문한 노드라면
    if DP[node][0] != 0 or DP[node][1] != 0:
        return DP[node]

    else:

        DP[node][0] = people[node-1]
        DP[node][1] = 0

        for leaf in table[node]:
            if isVisited[leaf] == False:
                isVisited[leaf] = True

                # 내가 불이 켜졌을 경우
                DP[node][0] += DFS(leaf)[1]
                # 내가 불이 꺼졌을경우
                DP[node][1] += max(DFS(leaf))

        return DP[node]

print(max(DFS(1)))
