import sys
sys.stdin = open('input.txt', "r")

'''
해빈이는 가지고 있는 캐릭터를 D일동안 훈련 시킨다.
캐릭터의 레벨은 1<= ? <= N
해빈이는 하루에 한 캐릭터를 고를 수 있다.
레벨은 1씩 오른다
안하고 쉴수도 있음.

해빈이가 가지고 있는 캐릭터의 수가 각 레벨 별로 주어진다.
이때 적절히 훈련을 시켜서 캐릭터의 힘의 합을 최대로 만드는 프로그램을 만들어라.
'''
N = int(sys.stdin.readline().rstrip())
level = list(map(int, sys.stdin.readline().rstrip().split()))
power = list(map(int, sys.stdin.readline().rstrip().split()))
D = int(sys.stdin.readline().rstrip())

DP = [0]*(D+1)

hap = 0
for a,b in zip(level,power):
    hap += a*b
    
def maximum(x,day):
    cnt = 1
    hap = level[x]
    #print('###',x,x-day)
    for idx in range (x-1,x-day,-1):
        if idx < 0 :
            break
        print(idx)
        hap += level[idx] // cnt
        cnt += 1
    return hap


for day in range (1,D+1):
    for idx in range (N-1):
        #TODO 레벨에 도착할수 있는지 확인 해야함.
        DP[day] = max(DP[day],DP[day-1]+power[idx+1]-power[idx])
    
    print(DP)
maximum(5,1)
    