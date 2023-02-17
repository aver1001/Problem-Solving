import sys
sys.stdin = open('input.txt', "r")
'''

A, B, C는 게임 시작 전 우승을 위해 필요한 승수와 경기 진행 순서를 미리 합의한다. 경기 진행 순서가 A, B, C라고 가정하자.
먼저 A와 B가 경기를 진행해 승자를 결정한다. 만약 두 사람이 같은 손동작을 내어 무승부가 발생할 경우 경기 진행 순서상 뒤인 사람이 이긴 것으로 간주한다. 즉 A와 B가 같은 손동작을 내면 B의 승리, A와 C가 같은 손동작을 내면 C의 승리, B와 C가 같은 손동작을 내면 C의 승리이다. 
이전 경기의 승자와 이전 경기에 참여하지 않은 사람이 경기를 진행해 승자를 결정한다.
특정 사람이 미리 합의된 승수를 달성할 때 까지 3을 반복한다.
합의된 승수를 최초로 달성한 사람이 우승한다.

'''

N,K = map(int, sys.stdin.readline().rstrip().split()) # 손동작수 N, 승수 K
winCal = []
for _ in range (N): #상성 입력
    # 2 승리, 1 무승부, 0 패배
    winCal.append(list(map(int, sys.stdin.readline().rstrip().split()))) # 손동작수 N, 승수 K

table = {}
table[0] = [[0,1,2] for _ in range (20)]
table[1] = list(map(int, sys.stdin.readline().rstrip().split())) # kh
table[2] = list(map(int, sys.stdin.readline().rstrip().split())) # mh

def fight(U1:int,U2:int,v:int,userScore:list) -> bool:
    
    state = False
    nextUser = findNextUser(U1,U2)
    
    #지우가 경기를 할 경우
    if U1 == 0:
        for u in (0,1,2):
            if winCal[u][table[U2][v]] == 2:
        
                if userScore[U1]+1 == K:
                    if U1 == 0:
                        return True
                    else:
                        return False
                userScore[U1] += 1
                state = state | fight(U1,nextUser,v+1,userScore)
                userScore[U1] -= 1
            #무승부 or U2 승리
            if winCal[u][table[U2][v]] == 1 or winCal[u][table[U2][v]] == 0:
                if userScore[U2]+1 == K:
                    if U2 == 0:
                        return True
                    else:
                        return False
                userScore[U2] += 1
                state = state | fight(U2,nextUser,v+1,userScore)
                userScore[U2] -= 1
    if U2 == 0:
        for u in (0,1,2):
            if winCal[table[U1][v]][u] == 2:
        
                if userScore[U1]+1 == K:
                    if U1 == 0:
                        return True
                    else:
                        return False
                userScore[U1] += 1
                state = state | fight(U1,nextUser,v+1,userScore)
                userScore[U1] -= 1
            #무승부 or U2 승리
            if winCal[table[U1][v]][u] == 1 or winCal[table[U1][v]][u] == 0:
                if userScore[U2]+1 == K:
                    if U2 == 0:
                        return True
                    else:
                        return False
                userScore[U2] += 1
                state = state | fight(U2,nextUser,v+1,userScore)
                userScore[U2] -= 1
    
    #지우가 경기를 하지 않을경우
    #U1 승리
    if winCal[table[U1][v]][table[U2][v]] == 2:
        
        if userScore[U1]+1 == K:
            if U1 == 0:
                return True
            else:
                return False
        userScore[U1] += 1
        state = state | fight(U1,nextUser,v+1,userScore)
        userScore[U1] -= 1
    #무승부 or U2 승리
    if winCal[table[U1][v]][table[U2][v]] == 1 or winCal[table[U1][v]][table[U2][v]] == 0:
        if userScore[U2]+1 == K:
            if U2 == 0:
                return True
            else:
                return False
        
        userScore[U2] += 1
        state = state | fight(U2,nextUser,v+1,userScore)
        userScore[U2] -= 1
        
    return state
    
def findNextUser(U1:int,U2:int) -> int:
    check = {0,1,2}
    check.remove(U1)
    check.remove(U2)
    
    return check.pop()

fight(0,1,0,[0,0,0])
print(table[0])