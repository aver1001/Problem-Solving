import sys
sys.stdin = open('input.txt', "r")

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())

PrimeNumber = {2,3,5,7,11,13,17,19,23,29,31,37,41}

DP = [[[-1]*18 for _ in range (18)] for _ in range (18)]
cnt = 0
def DFS(scoreA,scoreB,persenct,time):
    global cnt
    cnt += 1
    print(cnt)
    if time == 18:
        if scoreA in PrimeNumber or scoreB in PrimeNumber:
            return persenct
        else:
            return 0
    if DP[scoreA][scoreB][time] != -1:
        return DP[scoreA][scoreB][time]
    ret = 0
        
    #둘다 한골도 못 넣엇을 경우
    ret += DFS(scoreA,scoreB,persenct*(100-A)/100*(100-B)/100,time+1)
    #A만 한골 넣엇을 경우
    ret += DFS(scoreA+1,scoreB,persenct*A/100*(100-B)/100,time+1)
    #B만 한골 넣었을 경우
    ret += DFS(scoreA,scoreB+1,persenct*(100-A)/100*B/100,time+1)
    #둘다 골 넣었을 경우
    ret += DFS(scoreA+1,scoreB+1,persenct*A/100*B/100,time+1)

    DP[scoreA][scoreB][time] = ret
    return ret

print(DFS(0,0,1,0))