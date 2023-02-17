import sys
from itertools import permutations
sys.stdin = open('input.txt', "r")
'''

A, B, C는 게임 시작 전 우승을 위해 필요한 승수와 경기 진행 순서를 미리 합의한다. 경기 진행 순서가 A, B, C라고 가정하자.
먼저 A와 B가 경기를 진행해 승자를 결정한다. 만약 두 사람이 같은 손동작을 내어 무승부가 발생할 경우 경기 진행 순서상 뒤인 사람이 이긴 것으로 간주한다. 즉 A와 B가 같은 손동작을 내면 B의 승리, A와 C가 같은 손동작을 내면 C의 승리, B와 C가 같은 손동작을 내면 C의 승리이다. 
이전 경기의 승자와 이전 경기에 참여하지 않은 사람이 경기를 진행해 승자를 결정한다.
특정 사람이 미리 합의된 승수를 달성할 때 까지 3을 반복한다.
합의된 승수를 최초로 달성한 사람이 우승한다.

경기 순서는 지우 경희 민호 순서로 진행한다.
입력은         경희 민호 순서로 주어진다.
'''

N,K = map(int, sys.stdin.readline().rstrip().split()) # 손동작수 N, 승수 K
winCal = []
for _ in range (N): #상성 입력
    # 2 승리, 1 무승부, 0 패배
    winCal.append(list(map(int, sys.stdin.readline().rstrip().split()))) # 손동작수 N, 승수 K

table = {1:[],2:[]}
for num in list(map(int, sys.stdin.readline().rstrip().split())):
    table[1].append(num-1)
for num in list(map(int, sys.stdin.readline().rstrip().split())):
    table[2].append(num-1)
    
def simulation(u1,u2,v,winCnt):
    if Cnt[0] >= N:
        return False
    u3 = findNextUser(u1,u2)
    state = False
    #u1이 승리했을경우
    if (winCal[table[u1][Cnt[u1]]][table[u2][Cnt[u2]]] == 2 or (winCal[table[u1][Cnt[u1]]][table[u2][Cnt[u2]]] == 1 and u1 > u2)):
        Cnt[u1] += 1
        Cnt[u2] += 1
        if winCnt[u1]+1 >= K:
            if u1 == 0:
                return True
            else:
                return False
        winCnt[u1] += 1
        state = state | simulation(u1,u3,v+1,winCnt)
        winCnt[u1] -= 1
    #u2가 승리했을경우
    else:
        Cnt[u1] += 1
        Cnt[u2] += 1
        if winCnt[u2]+1 >= K:
            if u2 == 0:
                return True
            else:
                return False
        winCnt[u2] += 1
        state = state | simulation(u2,u3,v+1,winCnt)
        winCnt[u2] -= 1
        
        
    return state


def findNextUser(U1:int,U2:int) -> int:
    check = {0,1,2}
    check.remove(U1)
    check.remove(U2)
    
    return check.pop()
#print(list(permutations(range(N),N)))
#print(table[1])
#print(table[2])
for p in (permutations(range(N),N)):
    table[0] = p
    Cnt = [0,0,0]
    if simulation(0,1,0,[0,0,0]):
        print(1)
        exit()
print(0)