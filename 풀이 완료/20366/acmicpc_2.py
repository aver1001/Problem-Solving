import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline())
snowBall = list(map(int,sys.stdin.readline().rstrip().split(' ')))
snowBall.sort()
#2개씩 뽑고
answer = sys.maxsize
for snowMan1_1 in range (N):
    for snowMan1_2 in range (snowMan1_1+1,N):
        
        firstHap = snowBall[snowMan1_2]+snowBall[snowMan1_1]
            
        lt = snowMan1_1 + 1
        rt = snowMan1_2 - 1
        while lt < rt:
            #print(lt,rt)
            sub = firstHap - (snowBall[lt] + snowBall[rt])
            answer = min(abs(sub),answer)
            
            #만약 뺀게 양수라면 두번쨰 눈사람이 커져야함.
            if (sub) > 0:
                lt += 1
            #만약 뺸게 음수라면 두번쨰 눈사람이 작아져야함
            else:
                rt -= 1

            
print(answer)
            