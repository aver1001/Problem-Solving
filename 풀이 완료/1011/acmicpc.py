import sys
sys.stdin = open('input.txt', "r")

def answer(dis):
    hap = 0
    add = 1
    cnt = 0
    while True:
        
        if hap+ add >= dis:
            break
        hap += add
        cnt += 1
        
        if hap+ add >= dis:
            break
        hap += add
        cnt += 1
        
        add += 1
    
    return cnt+1

T = int(sys.stdin.readline().rstrip())
for _ in range (T):
    
    X, Y = map(int, sys.stdin.readline().rstrip().split())
    print(answer(Y-X))
    
    
