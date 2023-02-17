import sys
sys.stdin = open('input.txt', "r")
from collections import deque
'''
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다.
즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.
세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.


첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다.
다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다.
이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다.
물론 사건의 전후 관계가 모순인 경우는 없다.
다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다.
다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다.
사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

s줄에 걸쳐 물음에 답한다.
각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1, 어떤지 모르면(유추할 수 없으면) 0을 출력한다.

'''

'''
위상정렬 알고리즘 사용해서 해결
'''

n, k = map(int, sys.stdin.readline().rstrip().split())

table = {i:{'in':set(),'out':set()} for i in range (1,n+1)}

for _ in range (k):
    # A가 B보다 먼져 일어남
    # A -> B
    A, B = map(int, sys.stdin.readline().rstrip().split())
    table[A]['out'].add(B)
    table[B]['in'].add(A)

queue = deque([])
for key,value in table.items():
    if len(value['in']) == 0:
        queue.append(key)
        
answer = {i : -1 for i in range (1,n+1)}

cnt = 0
while (queue):
    Loc = queue.popleft()
    cnt += 1


    for nextLoc in table[Loc]['out']:
        table[nextLoc]['in'].remove(Loc)
        if len(table[nextLoc]['in']) == 0:
            answer[nextLoc] = cnt
            queue.append(nextLoc)
    
s = int(sys.stdin.readline().rstrip())

for _ in range (s):
    #앞에 있는 사건이 먼저 일어났으면 -1
    #뒤에 있는 사건이 먼저 일어났으면 1
    #알수 없다면 0을 출력한다.
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if answer[A]-answer[B] < 0:
        print(-1)
    elif answer[A] == answer[B]:
        print(0)
    else:
        print(1)
    
    
    
# A -> B
    
    
