import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input.txt', "r")

'''
간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을때, 아래의 쿼리에 답해보도록 하자.
    - 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.

트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다 (2 <= N <= 10^5, 1 <= R <= N, 1<= Q <= 10^5)
이어 N-1줄에 걸쳐, U, V 형태로 트리에 속한 간선의 정보가 주어진다.
이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.
이에 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다.
입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.

'''

N, R, Q = map(int, sys.stdin.readline().rstrip().split())
table = {i:set() for i in range (1, N+1)}

for _ in range (N-1):
    U,V = map(int, sys.stdin.readline().rstrip().split())
    table[U].add(V)
    table[V].add(U)
    
isVisited = [False]*(N+1)
answer = [0]*(N+1)

def findLeaf(x):
    hap = 1
    for nextNode in table[x]:
        if isVisited[nextNode] == False:
            isVisited[nextNode] = True
            hap += findLeaf(nextNode)
            
    answer[x] = hap

    return hap
isVisited[R] = True
findLeaf(R)

for _ in range (Q):
    query = int(sys.stdin.readline().rstrip())
    print(answer[query])
