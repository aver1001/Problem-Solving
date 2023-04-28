import sys
import heapq
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split())
start, end = map(int, sys.stdin.readline().rstrip().split())

table = {}

def tableInsert(h1,h2,k):
    table[h1][h2] = k
    table[h2][h1] = k
    

for i in range (N+1):
    table[i] ={}

for _ in range (M):
    tableInsert(*map(int, sys.stdin.readline().rstrip().split()))

weight = [0]*(N+1)
heap = [[-1_000_000, start]]
weight[start] = 1_000_000

cnt = 0

while heap:
    w,loc = heapq.heappop(heap)
    w = -w
    
    if loc == end:
        print(w)
        exit()
    
    cnt += 1
    
    
    for nextLoc, nextWeight in table[loc].items():
        minWeight = min(nextWeight, w)
        
        if weight[nextLoc] < minWeight:
            weight[nextLoc] = minWeight
            heapq.heappush(heap,[-minWeight,nextLoc])
print(weight[end])