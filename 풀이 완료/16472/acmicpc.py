import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
strs = sys.stdin.readline().rstrip()

def dictAdd(s:str):
    if s in table:
        table[s] += 1
    else:
        table[s] = 1

def dictPop(s:str):
    if table[s] == 1:
        del table[s]
    else:
        table[s] -= 1

table = {}

for idx in range (N):
    dictAdd(strs[idx])

lt = 0
rt = N
answer = 0

while rt < len(strs):
    dictAdd(strs[rt])
    
    while len(table) > N:
        dictPop(strs[lt])
        lt += 1
    # print(lt,rt)
    # print(table)
    answer = max(answer,rt-lt+1)
    rt += 1
print(answer)