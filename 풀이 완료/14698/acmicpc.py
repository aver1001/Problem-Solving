import sys
import heapq
sys.stdin = open('input.txt', "r")

def solution(heap):
    answer = 1
    while len(heap) != 1:
        energy = heapq.heappop(heap)*heapq.heappop(heap)
        answer = answer * energy % 1_000_000_007
        heapq.heappush(heap,energy)
    return answer

T = int(sys.stdin.readline().rstrip())
for _ in range (T):
    N = int(sys.stdin.readline().rstrip())
    heap = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heapify(heap)
    print(solution(heap))
    
