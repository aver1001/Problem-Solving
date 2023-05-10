import sys
sys.stdin = open('input.txt', "r")

N,M = map(int, sys.stdin.readline().rstrip().split())
price = []
prefixSum = [0]*(N+1)
prefixMin = [0]*(N+1)
for idx in range (N):
    price.append(int(sys.stdin.readline().rstrip()))
    
for idx in range (1,N+1):
    prefixSum[idx] = price[idx-1] + prefixSum[idx-1]


check=2000
for i in range(1,N+1):
    '''
    a ~ b 까지의 누적합을 구하고 싶다면 
    prefix[a] - prefix[b-1]로 구할수 있다.
    하지만 문제에서는 prefix[b-1], prefix[b-2]...의 최솟값을 구해야함.
    그로므로 DP를 만들어 prefix[b]의 최솟값을 저장해놓으면 됨.
    '''
    if i>=M:
        check=min(check,prefixSum[i-M])
        prefixMin[i]=max(prefixMin[i-1] , prefixSum[i]-check)
    else:
        prefixMin[i]=prefixMin[i-1]

print(prefixMin[-1])

