import sys
sys.stdin = open('input.txt', "r")

N,C = map(int, sys.stdin.readline().rstrip().split())
wegiht = list(map(int, sys.stdin.readline().rstrip().split()))

table ={0:1}
for i in wegiht:
    newTable = {0:1}
    for cost,cnt in table.items():
        if cost+i > C:
            continue
        
        if cost+i in table:
            newTable[cost+i] = cnt*2
        else:
            newTable[cost+i] = 1
    table = newTable
    

#print(table)
print(sum(table.values()))