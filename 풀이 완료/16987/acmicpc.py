import sys
sys.stdin = open('input.txt', "r")

'''
각 계란에는 내구도와 무게가 정해져있다.
계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다.
그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다.

1.  가장 왼쪽의 계란을 든다.
2.  손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
    단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
    이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
3.  가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
    단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
'''
N = int(sys.stdin.readline().rstrip())
eggs = []
for _ in range (N):
    S,W = map(int, sys.stdin.readline().rstrip().split())
    eggs.append([S,W])


answer = 0

def breakEgg(now:int,hap:int):
    global answer
    answer = max(hap,answer)
    if (now == N):
        return
    #들어야할 달걀이 깨져있다면 다음 계란으로 넘어감
    if eggs[now][0] <= 0:
        breakEgg(now+1,hap)
        return 
    
    for idx in range (N):
        #같은 계란끼리는 파괴불가능
        if idx == now:
            continue
        
        # 타겟 내구도가 0보다 작으면 진행할수 없음
        if eggs[idx][0] <= 0:
            continue
        # 계란치기 진행 
        eggs[now][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[now][1]
        nHap = hap
        if eggs[now][0] <= 0:
            nHap += 1
        if eggs[idx][0] <= 0:
            nHap += 1
        breakEgg(now+1,nHap)
        
        # 계란치기 복구
        eggs[now][0] += eggs[idx][1]
        eggs[idx][0] += eggs[now][1]


breakEgg(0,0)
print(answer)