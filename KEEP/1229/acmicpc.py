import sys
import time
sys.stdin = open('input.txt', "r")

start = time.time()

N = int(sys.stdin.readline().rstrip())

def hexagonPoint(x):
    if x <= 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return 6*(x-1)
    
def hexagonalNumber(x):
    table = [0]*x
    table[0] = 0
    table[1] = 1
    table[2] = 6

    for idx in range (3,x):
        table[idx] = table[idx-1] + hexagonPoint(idx) - (2*(idx-1)-1)

    
    return table
    
H = hexagonalNumber(708)

DP = [i for i in range (N+1)]

for i in range (2,708):
        
    for j in range (H[i],min(6*H[i],N+1)):
        DP[j] = min(DP[j-H[i]] + 1,DP[j])
print(DP[-1])
print(time.time()-start)

    

