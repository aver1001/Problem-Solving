import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
water = list(map(int, sys.stdin.readline().rstrip().split()))

## 투포인터

lt = 0
rt = N-1
Min = sys.maxsize

while lt < rt:
    
    if Min > abs(water[lt]+water[rt]):
        Min = abs(water[lt]+water[rt])
        answer = [water[lt],water[rt]]
    
    #두 용액의 합이 양수일경우
    if water[lt]+water[rt] > 0:
        rt -= 1
    #두 용액의 합이 음수일경우
    elif water[lt] + water[rt] < 0:
        lt += 1
    #두 용액의 합이 0일경우
    else:
        print(water[lt],water[rt])
        exit()
        
print(*answer)