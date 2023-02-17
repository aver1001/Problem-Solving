import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

def find(x) :

    if x >= M:
        
        return M
    
    if x != Root[x]:
        Root[x] = find(Root[x])
    return Root[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a>b:
        Root[b] = a
        return b
    else:
        Root[a] = b
        return a
        

N,M,K = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
Root = [i for i in range (M)]
C_cards = list(map(int, sys.stdin.readline().rstrip().split()))

cards.sort()
#print(' ',cards)

for target in C_cards:
    upperIdx = bisect_left(cards,target)
    #print('Target',target)
    
    if cards[upperIdx] <= target:
        upperIdx += 1
    
    if upperIdx >= M:
        upperIdx = 0
    #사용하지 않은 카드 일경우
    if Root[upperIdx] == upperIdx:
        #print('미사용')
        #그보다 큰거 사용
        print(cards[union(upperIdx,upperIdx+1)])
    #사용한 카드 일경우
    else:
        #print('사용')
        temp = find(upperIdx)
        print(cards[union(temp,temp+1)])
    #print(Root)