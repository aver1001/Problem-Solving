import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

MaxHeap = []
MinHeap = []


def insertHeap(num):
    # 값 찾아서 넣어주기
    if len(MaxHeap) == 0 and len(MinHeap) == 0:
        heapq.heappush(MinHeap, num)
        return
    else:
        if num < MinHeap[0]:
            heapq.heappush(MaxHeap, -num)
        else:
            heapq.heappush(MinHeap, num)

    # 비율 맞춰서 업데이트 해주기

    if len(MaxHeap) > len(MinHeap):
        heapq.heappush(MinHeap, -heapq.heappop(MaxHeap))
    elif len(MaxHeap) < len(MinHeap):
        heapq.heappush(MaxHeap, -heapq.heappop(MinHeap))


def printMiddleNum():
    if len(MaxHeap) >= len(MinHeap):
        print(-MaxHeap[0])
    elif len(MaxHeap) < len(MinHeap):
        print(MinHeap[0])


for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    insertHeap(num)
    printMiddleNum()
    # print(MaxHeap)
    # print(MinHeap)
