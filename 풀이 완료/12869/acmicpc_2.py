import sys
from itertools import permutations
sys.stdin = open('input.txt', "r")
'''
수빈이는 강호와 함꼐 스타크래프트를 하고 있다.

수빈이 뮤탈은 1개 남아있고
강호의 SCV는 N개 남아있다.

각각의 SCV는 남아있는 체력이 주어져 있으며, 뮤탈을 공격할수는 없다.
즉, 이 게임은 수빈이가 이겼다는 것이다.

뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.
    첫 번째로 공격받는 SCV는 체력 9를 잃는다.
    두 번째로 공격받는 SCV는 체력 3을 잃는다.
    세 번째로 공격받는 SCV는 체력 1을 잃는다.
    
SCV의 체력이 0 또는 그 이하가 되어버리면, SCV는 그 즉시 파괴된다. 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.
남아있는 SCV의 체력이 주어졌을 때, 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.
'''

'''
생각1
체력이 60을 넘어갈 수 없기 때문에 모든 경우의수가 그렇게 많지 않을 것 같음.
BFS 돌려버리면 어떨까?
'''

order = list(permutations([9, 3, 1], 3))
def answer(x, y, z, cnt):
    global ans
    print(x,y,z,cnt)
    if x <= 0 and y <= 0 and z <= 0:
        if ans > cnt:
            ans = cnt
            return

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    for i in order:
        answer(x - i[0], y - i[1], z - i[2], cnt + 1)


N = int(input())
a = list(map(int, input().split()))
while len(a) < 3:
    a += [0]
ans = 100
dp = [[[100] * (max(a) + 1) for i in range((max(a) + 1))] for j in range((max(a) + 1))]
answer(a[0], a[1], a[2], 0)
print(ans)