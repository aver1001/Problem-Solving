import sys
import heapq
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt', "r")

def dj(start : int):
    dis = [MAX_SIZE]*(n+1)
    dis[start] = 0
    heap = [(0,start)]
    while heap:
        nowTime,nowLoc = heapq.heappop(heap)
        
        for nextTime,nextLoc in table[nowLoc]:
            if nextTime+nowTime < dis[nextLoc]:
                dis[nextLoc] = nextTime+nowTime
                heapq.heappush(heap,(nextTime+nowTime,nextLoc))
    
    cnt = 0
    answer = 0
    for d in dis:
        if d == MAX_SIZE:
            continue
        cnt += 1
        answer = max(answer,d)
        
    return cnt,answer
T = int(sys.stdin.readline())

for _ in range (T):
    #컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    n,d,c = map(int, sys.stdin.readline().rstrip().split())
    MAX_SIZE = n*1000+1
    #print("해킹당한 컴퓨터 :", c)
    table = {i:[] for i in range (1,n+1)}
    timeCheck = [MAX_SIZE]*(n+1)
    for _ in range (d):
        #a가 b를 의존하며, 감염까지 s초 걸린다.
        a,b,s = map(int, sys.stdin.readline().rstrip().split())
        table[b].append((s,a))
    #print(table)
    
    print(*dj(c))

