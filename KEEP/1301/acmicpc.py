import sys
sys.stdin = open('input.txt', "r")
'''
다솜이는 자신의 목걸이를 구슬을 이용해서 만들려고 한다.
다솜이는 N 종류의 구슬을 가지고 있다. 서로 다른 종류의 구슬은 색이 다르다.
다솜이는 임의의 연속된 3개의 구슬의 색을 모두 다르게 하려고 한다.

예를들어 다솜일가 1번구슬을 2개, 2번구슬을 1개, 3번 구슬을 1개 가지고 있다고 하자.

'''
N = int(sys.stdin.readline().rstrip())
table = [0]*5
for idx in range (N):
    table[idx] = (int(sys.stdin.readline().rstrip()))

DP = [[[[[[[-1]*11 for _ in range (11)] for _ in range (11)] for _ in range (11)] for _ in range (11)] for _ in range (8)]for _ in range (8)]

def DFS(before1,before2,a,b,c,d,e):
    #print(before1,before2,a,b,c,d,e)
    if a == b == c == d == e == 0:
        return 1
    ret = DP[before1][before2][a][b][c][d][e]
    if ret != -1:
        return ret
    
    ret = 0
    
    if a != 0 and before1 != 0 and before2 != 0:
        ret += DFS(before2,0,a-1,b,c,d,e)
    if b != 0 and before1 != 1 and before2 != 1:
        ret += DFS(before2,1,a,b-1,c,d,e)
    if c != 0 and before1 != 2 and before2 != 2:
        ret += DFS(before2,2,a,b,c-1,d,e)
    if d != 0 and before1 != 3 and before2 != 3:
        ret += DFS(before2,3,a,b,c,d-1,e)
    if e != 0 and before1 != 4 and before2 != 4:
        ret += DFS(before2,4,a,b,c,d,e-1)

    DP[before1][before2][a][b][c][d][e] = ret
    return ret        
            
            
print(DFS(6,5,table[0],table[1],table[2],table[3],table[4]))
