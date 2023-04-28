import sys
import heapq
sys.stdin = open('input.txt', "r")


N = int(sys.stdin.readline().rstrip())
dis = []
for _ in range (N):
    dis.append(list(map(int, sys.stdin.readline().rstrip().split())))

def printBoard(board):
    for i in board:
        print(i)

isVisited = [False]*N

heap = []
heapq.heappush(heap,(0,0))
hap = 0
while heap:
    cost,loc = heapq.heappop(heap)
    #print(loc)
    if isVisited[loc] == True:
        continue
    isVisited[loc] = True
    hap += cost
    for nextLoc in range (N):
        if loc == nextLoc:
            continue
        if isVisited[nextLoc] == False:
            heapq.heappush(heap,(dis[loc][nextLoc],nextLoc))

print(hap)