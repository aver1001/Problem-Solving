import sys
import heapq
sys.stdin = open('input.txt', "r")
'''
K개의 소수가 있다. 이때, 이 소수들 중에서 몇 개를 곱해서 얻게 되는 수들이 있을 것이다. 소수들을 선택할 때에는 같은 수를 선택해도 되며, 주어지는 소수 자체도 포함시키자.
예를 들어 세 소수가 2, 5, 7이었다면, 이러한 곱들을 오름차순으로 나타내 보면, 2, 4, 5, 7, 8, 10, 14, 16, 20, 25, 28, 32, 35, 등이 된다.
K개의 소수가 주어졌을 때, 이러한 소수의 곱들 중에서 N번째 수를 구해 보자. 단 정답은 2^31보다 작은 자연수이다.


첫째 줄에 K(1 ≤ K ≤ 100), N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 K개의 소수가 오름차순으로 주어진다. 같은 소수가 여러 번 주어지는 경우는 없으며, 주어지는 소수는 모두 541보다 작거나 같은 자연수이다.

첫째 줄에 문제에서 설명한 대로 소수의 곱을 나열했을 때, N번째 오는 것을 출력한다.

27
'''

'''
생각 1
소수의 곱은 중복될수가 없음.
그렇다면 공식이 있을수 밖에 없을듯.. 찾아보자

[2]     => 1    
[2,3]   => 5    
[2,3,5] => 13 
[2,5,7,11] => 
근데 찾아도 새로운것들이 중간에 들어가기때문에 섞여서 찿을 수 없음..


'''

n, q = map(int, sys.stdin.readline().rstrip().split())
commend = list(map(int,sys.stdin.readline().rstrip().split()))

def inputHeap(heap,num):
    #중복제거
    if num in check:
        return
    heapq.heappush(heap,num)
    check.add(num)
    #개수 넘어갔을경우 하나 빼줌
    if len(heap) > q:
        heapq.heappop(heap)
        

heap = commend[:]
heapq.heapify(heap)
check = set()

for _ in range (n):
    n = heapq.heappop(heap)

    for c in commend:
        heapq.heappush(heap,n*c)
        if n % c == 0:
            break
print(n)
print(heap)

