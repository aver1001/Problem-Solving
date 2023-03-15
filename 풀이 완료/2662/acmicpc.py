import sys
import heapq
sys.stdin = open('input.txt', "r")

def chooseCompany():
    pass

costList = []

N,M = map(int, sys.stdin.readline().rstrip().split())
investToCompany = [0]*(M+1)

for day in range (N):
    money = N
    gain = list(map(int, sys.stdin.readline().rstrip().split()))
    
    '''
    각 회사,금액별로 1원당의 가치가 높은것을 선택하는것이 가장 큰 효율을 내는 경우이다.
    '''
    for company in range(1,M+1):
        costList.append((gain[company]/(day+1),day+1,company))
    costList.sort(reverse=True)
print(costList)

stack = []

for costPerMomney, days,companyNum in costList:
    print(costPerMomney, days,companyNum)
    
    if money == 0:
        break
    # 이전 투자금액보다 더 높고,                       #투자할 금액이 남은 금액으로 가능할경우
    if investToCompany[companyNum] < days and money >= days - investToCompany[companyNum]: 
        #투자한것들을 stack에 넣어준다 돌려야 하기때문에 이전값들을 저장
        stack.append((money,companyNum,investToCompany[companyNum])) #이전금액, 선택된 회사, 이전투자금액
        #남은금액 뺴주고
        money = money - (days - investToCompany[companyNum])
        #투자금액을 바꿔준다
        investToCompany[companyNum] = days
    else:
        while stack:
            stack.pop()