import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
know = list(map(int, sys.stdin.readline().rstrip().split()))

if know == [0]:
    print(M)
    exit()
    
party = []
for _ in range (M):
    party.append(list(map(int, sys.stdin.readline().rstrip().split())))

root = [i for i in range (N+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        root[a] = root[b]
    else:
        root[b] = root[a]

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

for p in party:
    if p[0] == 1:
        continue
    
    start = p[1]
    
    for i in p[2:]:
        union(start,i)

knowPeople = set()
for k in know[1:]:
    knowPeople.add(find(k))
    
answer = 0
for pp in party:

    for p in pp[1:]:
        if find(p) in knowPeople:
            break
    else:
        answer += 1
        
print(answer)