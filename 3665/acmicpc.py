import sys
from collections import deque
sys.stdin = open('input.txt', "r")
T = int(sys.stdin.readline().rstrip())

for _ in range (T):
    N = int(sys.stdin.readline().rstrip())
    check = []
    before = list(map(int, sys.stdin.readline().rstrip().split()))
    table = {i : {'in':0,'out':set()} for i in range (1,N+1)}
    for i in range (N):
        for j in range (i+1,N):
            table[before[j]]['in']+=1
            table[before[i]]['out'].add(before[j])
    M = int(sys.stdin.readline().rstrip())
    
    for _ in range(M):
        A,B = map(int,sys.stdin.readline().rstrip().split())
        
        if B in table[A]['out']:
            table[A]['in'] += 1
            table[A]['out'].remove(B)
            table[B]['in'] -= 1
            table[B]['out'].add(A)
        else:
            table[B]['in'] += 1
            table[B]['out'].remove(A)
            table[A]['in'] -= 1
            table[A]['out'].add(B)
    
    #print()
    
    queue = deque([])
    for key,value in table.items():
        if value['in'] == 0:
            queue.append(key)
            
    answer = []
    while queue:
        t = queue.popleft()
        answer.append(t)
        
        for i in table[t]['out']:
            table[i]['in'] -= 1
            if table[i]['in'] == 0:
                queue.append(i)
                
    if len(answer)!= N:
        print('IMPOSSIBLE')
    else:
        print(*answer)