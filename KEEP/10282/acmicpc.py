import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt', "r")

def solution(node:int,time:int) -> int:
    global cnt
    if timeCheck[node] == MAX_SIZE:
        cnt += 1
    timeHap = time
    timeCheck[node] = time
    #times가 작은 순서로 탐색해야 함.
    for NextTime,nextNode in table[node]:
        if timeCheck[nextNode] >= time+NextTime:
            timeHap = max(solution(nextNode,time+NextTime),timeHap)
    return timeHap


T = int(sys.stdin.readline())

for _ in range (T):
    #컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    n,d,c = map(int, sys.stdin.readline().rstrip().split())
    MAX_SIZE = n*1000
    #print("해킹당한 컴퓨터 :", c)
    table = {i:[] for i in range (1,n+1)}
    timeCheck = [MAX_SIZE]*(n+1)
    for _ in range (d):
        #a가 b를 의존하며, 감염까지 s초 걸린다.
        a,b,s = map(int, sys.stdin.readline().rstrip().split())
        table[b].append((s,a))
        
    # for idx in range (1,n+1):
    #     table[idx].sort
    cnt = 0
    answer = solution(c,0)
    print(cnt,answer)
    #print(timeCheck)


