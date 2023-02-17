import sys
sys.stdin = open('input.txt', "r")

N = sys.stdin.readline().rstrip()

answer = [0]*10

if len(N) == 1:
    for i in range (1,int(N)+1):
        answer[i] += 1
    print(*answer)
    exit()
cnt = -1
for i in range (len(N)-1,-1,-1):
    cnt += 1
    left = N[:i]
    mid = N[i]
    right = N[i+1:]
    
    if left == '':
        #마지막자리
        for idx in range (int(mid)):
            answer[idx] += 10**cnt
        
        answer[int(mid)] += int(right)+1
        answer[0] -= 10**cnt
            
    elif right == '':
        #1의자리
        for idx in range (10):
            answer[idx] += int(left)
        for idx in range (int(mid)+1):
            answer[idx] += 1
        answer[0] -= 1
    else:
        for idx in range (10):
            answer[idx] += int(left) * (10**cnt)
        for idx in range (int(mid)):
            answer[idx] += 10**cnt

        answer[int(mid)] += int(right)+1
        answer[0] -= 10**cnt
        
    
        
            
print(*answer)
    
    