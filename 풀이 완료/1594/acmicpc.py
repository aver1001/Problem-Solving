import sys
sys.stdin = open('input.txt', "r")
'''
번호를 2개 또는 3개씩 묶는다
그룹은 3가지로 나뉜다
    오: 그룹에 들어있는 모든 숫자가 같은 숫자로 이루어진 경우다. 예를 들면 000, 77이다.
    걍: 그룹에 들어있는 숫자가 3자리 일 때, 두 숫자가 같은 경우다. 예를 들면 030, 229, 116이다.
    즐: 그룹에 들어있는 숫자가 모든 다른 경우이다. 예를 들면 123, 90이다.

전화번호에도 품질이 존재하는데, 품질의 정도는 다음과 같이 정할 수 있다.
2×(오 그룹에 들어가는 그룹의 개수) + (걍 그룹에 들어가는 그룹의 개수)

영식이의 핸드폰 전화번호가 주어졌을 때, 전화번호를 적절히 그룹으로 쪼개서,
영식이 전화번호의 품질이 최대인 전화번호를 출력하는 프로그램을 작성하시오.
'''
N = sys.stdin.readline().rstrip()

def getPrice(x):
    
    ret = 0
    if len(x) == 2:
        #모두 같은숫자
        if x[0] == x[1]:
            ret = 2
    
    else:
        if x[0] == x[1] == x[2]:
            ret =  2
        elif x[0] == x[1] or x[0] == x[2] or x[1]==x[2]:
            ret =  1
    
    return ret

answerDP = [[] for _ in range (len(N)+1)]

DP = [0]*(len(N)+1)
for idx in range (2,len(N)+1):
    if idx >= 2 and idx != 3:
        temp = DP[idx-2] + getPrice(N[idx-2:idx])
        if DP[idx] < temp:
            DP[idx] = temp
            answerDP[idx] = [idx-2]
        elif DP[idx] == temp :
            answerDP[idx].append(idx-2)
        #DP[idx] = max(DP[idx-2] + getPrice(N[idx-2:idx]),DP[idx])
    if idx >= 3 and idx != 4:
        temp = DP[idx-3]+ getPrice(N[idx-3:idx])
        if DP[idx] < temp:
            DP[idx] = temp
            answerDP[idx] = [idx-3]
        elif DP[idx] == temp:
            answerDP[idx].append(idx-3)
        
        #DP[idx] = max(DP[idx-3]+ getPrice(N[idx-3:idx]),DP[idx])

print(DP)
print(answerDP)
def findAnswer(x,temp):
    if x == len(N):
        print(temp[1:])
        exit()
    
    if x+2 <= len(N) and x in answerDP[x+2]:
        findAnswer(x+2,temp + '-'+N[x:x+2])
    if x+3 <= len(N) and x in answerDP[x+3]:
        findAnswer(x+3,temp + '-'+N[x:x+3])

findAnswer(0,'')
#findAnswer(1,'')