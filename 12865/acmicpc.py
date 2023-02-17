import sys
sys.stdin = open('input.txt', "r")

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가짐
# 준서는 K만큼의 무게만을 넣을수 있다

# 준서가 배낭에 넣을 수 있는 물건들의 가치의 최대값을 알려주자.


N, K = map(int, sys.stdin.readline().rstrip().split(' '))

table = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, sys.stdin.readline().rstrip().split(' '))

    for idx in range(1, K+1):
        if idx < W:
            table[i][idx] = table[i-1][idx]
        else:
            table[i][idx] = max(table[i][idx-W] + V, table[i-1][idx])

print(table[-1][-1])
