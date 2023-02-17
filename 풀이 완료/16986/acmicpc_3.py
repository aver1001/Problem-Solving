import sys
sys.stdin = open('input.txt', "r")
'''

A, B, C는 게임 시작 전 우승을 위해 필요한 승수와 경기 진행 순서를 미리 합의한다. 경기 진행 순서가 A, B, C라고 가정하자.
먼저 A와 B가 경기를 진행해 승자를 결정한다. 만약 두 사람이 같은 손동작을 내어 무승부가 발생할 경우 경기 진행 순서상 뒤인 사람이 이긴 것으로 간주한다. 즉 A와 B가 같은 손동작을 내면 B의 승리, A와 C가 같은 손동작을 내면 C의 승리, B와 C가 같은 손동작을 내면 C의 승리이다. 
이전 경기의 승자와 이전 경기에 참여하지 않은 사람이 경기를 진행해 승자를 결정한다.
특정 사람이 미리 합의된 승수를 달성할 때 까지 3을 반복한다.
합의된 승수를 최초로 달성한 사람이 우승한다.

지우가 모든 손동작을 다르게 내어!!!!

'''

N,K = map(int, sys.stdin.readline().rstrip().split()) # 손동작수 N, 승수 K
winCal = []
for _ in range (N): #상성 입력
    # 2 승리, 1 무승부, 0 패배
    winCal.append(list(map(int, sys.stdin.readline().rstrip().split()))) # 손동작수 N, 승수 K

table = {}
temp = []
for num in list(map(int, sys.stdin.readline().rstrip().split())):
    temp.append(num-1)
table[1] = temp
temp = []
for num in list(map(int, sys.stdin.readline().rstrip().split())):
    temp.append(num-1)
table[2] = temp

def fight(U1:int,U2:int,v:int,userScore:list,zewoo:int) -> bool:
    state = False
    nextUser = findNextUser(U1,U2)
    
    if U2 == 0:
        for i in range (N):
            if(zewoo & 1<<i != 0):  #만약 선택한 가위바위보라면 
                continue            #진행하지 않는다.
            if winCal[table[U1][v]][i] == 2:
                winner = U1
            elif winCal[table[U1][v]][i] == 1 or winCal[table[U1][v]][i] == 0:
                winner = U2
            
            if userScore[winner]+1 == K:
                if winner == 0:
                    return True
                else:
                    return False
            userScore[winner] += 1
            state | fight(U2,nextUser,v+1,userScore, zewoo|(1<<i))
            userScore[winner] -= 1
    elif U1 == 0:
        for i in range (N):
            if(zewoo & 1<<i != 0):  #만약 선택한 가위바위보라면 
                continue            #진행하지 않는다.
            if winCal[table[U2][v]][i] == 2:
                winner = U2
            elif winCal[table[U2][v]][i] == 1 or winCal[table[U2][v]][i] == 0:
                winner = U1
            
            if userScore[winner]+1 == K:
                if winner == 0:
                    return True
                else:
                    return False
            userScore[winner] += 1
            state | fight(U2,nextUser,v+1,userScore, zewoo|(1<<i))
    
            
    else:
        if winCal[table[U1][v]][table[U2][v]] == 2:
            winner = U1
        elif winCal[table[U1][v]][table[U2][v]] == 1 or winCal[table[U1][v]][table[U2][v]] == 0:
            winner = U2
            
        if userScore[winner]+1 == K:
            if winner == 0:
                return True
            else:
                return False
        userScore[winner] += 1
        state | fight(U2,nextUser,v+1,userScore, zewoo)
        userScore[winner] -= 1
    
    return state
    
def findNextUser(U1:int,U2:int) -> int:
    check = {0,1,2}
    check.remove(U1)
    check.remove(U2)
    
    return check.pop()

if (fight(0,1,0,[0,0,0],0)):
    print(1)
else:
    print(0)