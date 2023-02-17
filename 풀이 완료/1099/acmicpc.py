import sys
sys.stdin = open('input.txt', "r")

start = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
word = []
check = set()
for _ in range (N):
    word.append(sys.stdin.readline().rstrip())

DP = [sys.maxsize] * (len(start)+1)
DP[0] = 0
def isPossible(a,b):
    
    table = {}
    for t in a:
        if t in table:
            table[t] += 1
        else:
            table[t] = 1
        
    for t in b:
        if t in table:
            table[t] -= 1
            if table[t] == 0:
                del table[t]
        else:
            return False
    return True
    
def calCost(a,b):
    cost = 0
    for c,d, in zip(a,b):
        if c != d:
            cost += 1
    return cost
            

for idx in range (len(start)+1):
    for w in word:
        if idx - len(w) < 0:
            continue
        
        if isPossible(w,start[idx-len(w):idx]):

            if DP[idx-len(w)] == sys.maxsize:
                continue
            else:
                DP[idx] = min(DP[idx-len(w)]+calCost(w,start[idx-len(w):idx]),DP[idx])

if DP[-1] == sys.maxsize:
    print(-1)
else:
    print(DP[-1])