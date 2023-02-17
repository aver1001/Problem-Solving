import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline().rstrip())

table = {}

for _ in range (N-1):
    

    root, leaf, cost = map(int, sys.stdin.readline().rstrip().split())
    
    if root in table:
        table[root][leaf] = cost
    else:
        table[root] = {leaf : cost}

#print(table)

answer = 0


def DFS(node):
    global answer
    if node not in table:
        return 0
    
    temp = [0,0]
    
    for leaf,cost in table[node].items():
        
        temp.append(DFS(leaf)+cost)
        
    temp.sort()
    #print(node,temp)
    answer = max(answer,temp[-1]+temp[-2])
    return temp[-1]

DFS(1)
print(answer)