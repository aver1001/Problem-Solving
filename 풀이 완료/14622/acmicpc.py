import sys
sys.stdin = open('input.txt', "r")


#commend = sys.stdin.readline().rstrip().split(' ')

Prime= [True]* 5000000
Prime[0] = Prime[1] = False
    
for i in range (2,5000000):
    if Prime[i] == True:
        for j in range (2*i,5000000,i):
            Prime[j] = False
            
            
'''

두 사람이 번갈아가며 소수를 말한다.
소수가 아닌 수를 부르게 될 경우 상대방은 지금까지 상대방이 말한 소수중에서 3번째로 큰 수만큼 점수를 얻게 된다.(만약 상대방이 지금까지 말한 소수가 3개 미만이라면 상대방은 1000점을 얻게 된다.)
만약 지금까지 한번이라도 등장한 소수를 말할 경우 해당 소수를 말한 팀이 -1000을 얻게 되며 해당 소수는 그 사람이 말한 소수로 기록되지 않는다.
규성이는 도전자이므로 게임은 항상 대웅이부터 시작한다.
두 사람이 말할 수 있는 소수는 항상 5000000 미만이다.

'''
N = int(sys.stdin.readline().rstrip())
check = set()
Dscore = 0
Kscore = 0
Dlist = []
Klist = []

def ListAppend(list,num):
    if len(list) < 3:
        list.append(num)
    else:
        list.append(num)
        list.sort()
        list = list[1:]
    return list
    
for _ in range (N):
    D,K = map(int, sys.stdin.readline().rstrip().split())
    
    #대웅이가 소수를 불렀을경우
    if Prime[D]:
        #만약 지금까지 한번이라도 등장한 소수를 말할 경우
        if D in check:
            # 해당 소수를 말한 팀이 -1000을 얻게 되며 해당 소수는 그 사람이 말한 소수로 기록되지 않는다.
            Dscore -= 1000
        else:
            Dlist = ListAppend(Dlist,D)
            check.add(D)
    else:
        #소수가 아닌 수를 부르게 될 경우
        if len(Klist) < 3:
            # 만약 상대방이 지금까지 말한 소수가 3개 미만이라면 상대방은 1000점을 얻게 된다.
            Kscore += 1000
        else:
            # 상대방은 지금까지 상대방이 말한 소수중에서 3번째로 큰 수만큼 점수를 얻게 된다.
            Kscore += Klist[0]
            
    #규성이가 소수를 불렀을경우
    if Prime[K]:
        #한번이라도 등장한 소수를 말했을 경우
        if K in check:
            Kscore -= 1000
        else:
            Klist = ListAppend(Klist,K)
            check.add(K)
    else:
        if len(Dlist) < 3:
            Dscore += 1000
        else:
            Dscore += Dlist[0]
            
    #print(Dlist,Dscore,'||',Klist,Kscore)
            
if Dscore> Kscore:
    print('소수의 신 갓대웅')
elif Dscore == Kscore :
    print('우열을 가릴 수 없음')
else:
    print('소수 마스터 갓규성')