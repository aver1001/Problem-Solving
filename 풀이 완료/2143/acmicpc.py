import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
nList = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
mList = list(map(int, sys.stdin.readline().rstrip().split()))
'''
한 배열 A[1], A[2]... A[n]에 대해서
부 배열은 A[i], A[i+1],... ,A[j-1],A[j] 를 말한다.
이런 부 배열의 합은 A[i] + ... A[j]를 의미한다.

각 원소가 정수인 두 배열 A[1], ..., A[n]과 B[1],...B[m]이 주어졌을때
A의 부배열의 합에 B부배열의 합을 더해서 T 가 되는 모든 부 배열 쌍의 개수를 구하여라.

n < 1000 , m <1000
'''

# 투포인터로 각각의 부배열의 경우를 구해보자. 
# 이 경우 최악의 경우 1000^2 == 1000000 == 백만 연산이 필요하고
# 각각의 부배열을 구하게 된다면 2백만의 연산이 필요하다. 충분히 가능한 연산.

def insertDict(d,num):
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

def childArr(Arr,N) :
    lt, rt = 0,0
    table = {}
    
    while lt != N:
        hap = 0
        
        while rt != N:
            hap += Arr[rt]
            insertDict(table,hap)
            rt += 1
            
        lt += 1
        rt = lt
    return table

    
    
nDict = childArr(nList,n)
mDict = childArr(mList,m)
answer = 0


for key in nDict:
    #더해서 T가 되는게 있다면.
    if T-key in mDict:
        answer += nDict[key] * mDict[T-key]
print(answer)