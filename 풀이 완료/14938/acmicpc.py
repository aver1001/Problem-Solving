import sys
sys.stdin = open('input.txt', "r")

# 지역의 개수 n (1 ≤ n ≤ 100)
# 예은이의 수색범위 m (1 ≤ m ≤ 15)
# 길의 개수 r (1 ≤ r ≤ 100)
n, m, r = map(int, sys.stdin.readline().rstrip().split())
cost = list(map(int, sys.stdin.readline().rstrip().split()))

'''
플루이드 워샬 써서 모든 거리의 최소값을 구한다.
지역의 개수 100^3 = 1000000 백만이므로 충분히 가능

그뒤 각 지역을 순회하면서 수색거리가 m보다 작은것들만 더해서 최대값을 구하면 됨.
'''

def boardPrint(board):
    for i in board:
        print(i)
    print()

def floydWarshall(n,distance):
    for k in range (n):
        for i in range (n):
            for j in range (n):
                distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])

def calMaximum(n,m):
    answer = 0
    for loc in range (n):
        hap = 0
        for nextLoc in range (n):
            
            if distance[loc][nextLoc] <= m:
                hap += cost[nextLoc]
        
        answer = max(answer,hap)
    return answer


distance = [[sys.maxsize]*n for _ in range (n)]
for i in range (n):
    distance[i][i] = 0
    
for _ in range (r):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    distance[a][b] = c
    distance[b][a] = c


floydWarshall(n,distance)
print(calMaximum(n,m))

# boardPrint(distance)
# print(cost)