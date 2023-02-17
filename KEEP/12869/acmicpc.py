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
DP = [[[-1]*61 for _ in range (61)] for _ in range (61)]
N = int(sys.stdin.readline().rstrip())
SCVS = [0,0,0]
temp = list(map(int,sys.stdin.readline().rstrip().split()))
for idx in range (len(temp)):
    SCVS[idx] =temp [idx]
    
order = list(permutations([9,3,1],3))

answer = 19
def DFS(SCV,cnt):
    global answer
    
    if all(num <= 0 for num in SCV):
        if answer > cnt:
            answer = cnt
            return
        
    if DP[SCV[0]][SCV[1]][SCV[2]] != -1:
        return
    
    DP[SCV[0]][SCV[1]][SCV[2]] = cnt
    
    for o in order:
        print(o)
        print(SCV)
        temp = [SCV[0]-o[0],SCV[1]-o[1],SCV[2]-o[2]]
        print(temp)
        for idx in range (3):
            if temp[idx] < 0:
                temp[idx] = 0
        
        DFS(temp,cnt+1),answer

DFS(SCVS,0)  
print(answer)
        