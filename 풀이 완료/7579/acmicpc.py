import sys
sys.stdin = open('input.txt', "r")
'''
우리는 여러가지 앱을 사용한다.
대개의 경우 화면에 보이는 '실행중'인 앱은 하나뿐이지만, 보이지 않은 상태로 많은 앱이 '활성화'되어있다.
활성화 == 화면에 보이지 않더라도 메인메모리에 직전의 상태가 기록되어 있음.

N개의 앱이 활성화 되어있다고 가정하자.
Ai 는 mi 바이트만큼의 메모리를 사용하고 있다.
또한 Ai 를 비활성화 한 후에 다시 실행하고자 할 경우 추가적으로 들어가는 비용을 ci라고 하자.
이러한 상황에서 사용자가 새로운 앱 B를 실행하고자 하여, 추가로 M바이트의 메모리가 필요하다고 하자.
현재 활성화 되어있는 앱 중에서 몇 개를 비활성화 하여 M바이트 이상의 메모리를 추가로 확보해야 한다.
여러분들은 그중에서 비활성화 했을 경우 비용 ci의 합을 최소화하여 필요한 메모리 M바이트를 확보하는 방법을 찾아야 한다.

'''

N,M = map(int, sys.stdin.readline().rstrip().split())
m = list(map(int, sys.stdin.readline().rstrip().split()))
c = list(map(int, sys.stdin.readline().rstrip().split()))
DP = [[0]*(N+1) for _ in range (N+1)]

for i in DP:
    print(i)
    
for idx,(memory,cost) in enumerate(zip(m,c)):
    print(idx,memory,cost)