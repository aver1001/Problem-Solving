import sys
sys.stdin = open('input.txt', "r")


T = int(sys.stdin.readline().rstrip())


'''
연결된 두 동그라미의 경우 색이 달라야 한다.
사이클이 존재하냐? 
근데 사이클이 존재해도 가능할수도 있음.

그냥 그래프를 연결해놓고 순회하는건? 가능할듯.

'''

def DFS(Loc,c):
    check[Loc] = c
    
    for nextLoc in table[Loc]:
        if check[nextLoc] == -1:
            DFS(nextLoc,not c)
            continue
        if check[nextLoc] == (not c):
            continue
        else:
            return False
        
    return True
        
    
    
    

for _ in range (T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    table = {i:set() for i in range (1,n+1)}
    for _ in range (m):
        x,y = map(int, sys.stdin.readline().rstrip().split())
        table[x].add(y)
        table[y].add(x)
    
    check = [-1]*(n+1)
    
    for idx in range (1,n+1):
        if check[idx] == -1:
            if DFS(idx,0):
                continue
            else:
                print('impossible')
                break
    else:
        print('possible')
            

