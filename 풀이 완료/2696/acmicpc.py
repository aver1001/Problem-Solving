import sys
import heapq
sys.stdin = open('input.txt', "r")


def inputHeap(num):

    if len(maxHeap) == 0:
        heapq.heappush(maxHeap, -num)
        return

    if len(minHeap) == 0:
        if -maxHeap[0] >= num:
            temp = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, temp)
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)
        return

    if num >= -maxHeap[0]:

        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, -num)

    if len(maxHeap) < len(minHeap):
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))
    elif len(maxHeap) > len(minHeap):
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    return


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = []
    for _ in range(N//10 + 1):
        numbers.extend(
            list(map(int, sys.stdin.readline().rstrip().split(' '))))
    maxHeap = []
    minHeap = []
    answer = []
    for idx in range(1, N+1):
        inputHeap(numbers[idx-1])
        # 홀수일경우
        if idx % 2 != 0:
            if len(maxHeap) > len(minHeap):
                answer.append(-maxHeap[0])
            else:
                answer.append(minHeap[0])
    print(len(answer))
    for idx in range(0, len(answer), 10):
        print(*answer[idx:idx+10])
