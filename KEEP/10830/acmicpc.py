import sys
sys.stdin = open('input.txt', "r")


T = int(sys.stdin.readline().rstrip())

table = {chr(i) : set() for i in range (65,91)}
for i in range (97,123):
    table[chr(i)] = set()
    
for _ in range (T):
    A,B = sys.stdin.readline().rstrip().split(' => ')
    table[A].add(B)
    
answer = set()

def DFS(root,char):
    if check[char] == 1:
        return
    answer.add((root,char))
    check[char] = 1
    for i in range (65,91):
        if i == char:
            continue
        if chr(i) in table[chr(char)]:
            DFS(root,i)
        
    
    for i in range (97,123):
        if i == char:
            continue
        if chr(i) in table[chr(char)]:
            DFS(root,i)

for i in range (65,91):
    check = [0]*150
    DFS(i,i)
    
for i in range (97,123):
    check = [0]*150
    DFS(i,i)
answer = list(answer)
answer.sort()
cnt = 0
for a,b in answer:
    if a!= b:
        cnt += 1
print(cnt)
for a,b in answer:
    if a!= b:   
        print(chr(a),'=>',chr(b))
    