import sys
from collections import deque
sys.stdin = open('input.txt', "r")

'''
수행해야 할 작업 N개가 있다 (3~10000)
각각의 작업마다 걸리는 시간(1~100)이 정수로 주어진다.

몇몇의 작업들에게는 선행관계가 있다.

모든 작업을 완료하기 위해 필요한 최소 시간을 구하여라.
선행관계가 없는 작업은 동시수행이 가능하다.
'''

N = int(sys.stdin.readline())

table = {i:{'cost':0,'cnt':0,'in':set(),'out':set()} for i in range (1,N+1)}

for idx in range (1,N+1):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    table[idx]['cost'] = inputs[0]
    table[idx]['cnt'] = inputs[1]
    for j in range (2,2+inputs[1]):
        table[inputs[j]]['out'].add(idx)
        table[idx]['in'].add(inputs[j])
        

queue = deque([])
DP = [0]*(N+1)
for key,value in table.items():
    if value['cnt'] == 0:
        queue.append(key)
        DP[key] = value['cost']
        
while queue:
    nowLoc = queue.popleft()
    
    for idx in (table[nowLoc]['in']):
        DP[nowLoc] = max(DP[nowLoc],DP[idx]+table[nowLoc]['cost'])
    
    for nextLoc in table[nowLoc]['out']:
        nextCost = table[nextLoc]['cost']
        table[nextLoc]['cnt'] -= 1
        
        if table[nextLoc]['cnt'] == 0:
            queue.append((nextLoc))
            
#print(DP)
print(max(DP))