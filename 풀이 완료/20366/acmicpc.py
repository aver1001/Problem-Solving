import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline())
snowBall = list(map(int,sys.stdin.readline().rstrip().split(' ')))
snowBall.sort()
#2개씩 뽑고
for (snowMan1_1,snowMan1_2) in combinations(c,2):
    #조합하나씩 뽑아서 2pointer?
    # 두 눈사람의 키의 차이가 작을수록 두 눈사람의 사이가 좋다고 판단
    firstHap = snowMan1_2,snowMan1_1
    lt = 0
    rt = 1
    
    while True:
        sub = firstHap - (snowBall[lt] + snowBall[rt])
        #만약 뺀게 양수라면 두번쨰 눈사람이 커져야함.
        if (sub) > 0:
            rt += 1
        #만약 뺸게 음수라면 두번쨰 눈사람이 작아져야함
        elif (sub) < 0:
            lt += 1
        #뺀게 같다면 
        else: 
            print(0)
            exit()
        #기저조건
        
    
