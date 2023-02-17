import sys
import heapq
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    N = int(sys.stdin.readline().rstrip())
    fileList = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    heapq.heapify(fileList)
    answer = 0

    while len(fileList) >= 2:
        file1 = heapq.heappop(fileList)
        file2 = heapq.heappop(fileList)

        mixFile = file1 + file2
        answer += mixFile
        heapq.heappush(fileList, mixFile)

    print(answer)
