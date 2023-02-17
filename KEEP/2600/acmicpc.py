import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input.txt', "r")

'''
두 사람 A,B가 번갈아 가면서 두 개의 구슬 통에서 몇 개씩의 구슬을 꺼내는 게임을 한다.

한번에 한사람이 한통에서 꺼낼수 있는 구슬의 개수는 3가지 뿐이다.
구슬을 꺼낼 경우 두 개의 구슬 통 중에서 하나를 마음대로 선택해서 그 안에서만 꺼낼 수 있다.

게임은 항상 A가 먼저 하고 그 다음 B .. 반복
자신의 차례가 되었을때 정해진 규칙대로 구슬을 꺼낼 수 없는 사람이 패배

1 <= b1 < b2 < b3 <= 30
1 <= k1,k2 <= 500

'''

b1,b2,b3 = map(int, sys.stdin.readline().rstrip().split())
temp = [b1,b2,b3]

def DFS(k1,k2,p):
    #B가 한번이라도 이기면 나는 무조건 짐
    if DP[k1][k2][p] != -1:
        return DP[k1][k2][p]
    
    for sub in temp:
        if sub <= k1 and not DFS(k1-sub,k2, not p):
            DP[k1][k2][p] = True
            return DP[k1][k2][p]
            
        if sub <= k2 and not DFS(k1,k2-sub, not p):
            DP[k1][k2][p] = True
            return DP[k1][k2][p]
        
    DP[k1][k2][p] = False
    return DP[k1][k2][p]
            

#게임이론
'''
A가 이기는 경우의수가 1개라도 존재한다 == A승리
A가 한번도 이기지 못한다 == B승리
'''
for _ in range (5):
    k1,k2 = map(int, sys.stdin.readline().rstrip().split())
    DP = [[[-1]*2 for _ in range (501)]for _ in range (501)]
    if DFS(k1,k2,False) :
        print('A')
    else:
        print('B')    
    
'''
A B A A B
'''