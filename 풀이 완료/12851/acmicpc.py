import sys
from collections import deque
import time as tt
sys.stdin = open('input.txt', "r")
'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고,
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
'''
N, K = map(int, sys.stdin.readline().rstrip().split())


queue = deque([[N,1]])
length = 100000
timeCheck = [0]*length
timeCheck[N] = 1

answer = 0
while queue:
    nextLoc,time = queue.popleft()
    #print(timeCheck)
    #print(queue)
    #tt.sleep(0.5)

    #1초 후에 X+1로 이동
    if nextLoc+1 < length-1 and timeCheck[nextLoc+1]  == 0 or timeCheck[nextLoc+1] >= time+1:
        if nextLoc+1 == K:
            if timeCheck[nextLoc+1] == time+1:
                answer += 1
            elif timeCheck[nextLoc+1] == 0 or timeCheck[nextLoc+1] > time +1:
                timeCheck[nextLoc+1] = time+1
                answer = 1
            continue
        timeCheck[nextLoc+1] = time+1
        queue.append([nextLoc+1,time+1])
    
    #1초 후에 X-1로 이동
    if nextLoc-1 >= 0 and (timeCheck[nextLoc-1]  == 0 or timeCheck[nextLoc-1] >= time+1):
        if nextLoc-1 == K:
            if timeCheck[nextLoc-1] == time+1:
                answer += 1
            elif timeCheck[nextLoc-1] == 0 or timeCheck[nextLoc-1] > time +1:
                timeCheck[nextLoc-1] = time+1
                answer = 1
            continue
        timeCheck[nextLoc-1] = time+1
        queue.append([nextLoc-1,time+1])
    
    #1초 후에 2*X로 이동
    if nextLoc*2 < length-1 and (timeCheck[nextLoc*2]  == 0 or timeCheck[nextLoc*2] >= time+1):
        if nextLoc*2 == K:
            if timeCheck[nextLoc*2] == time+1:
                answer += 1
            elif timeCheck[nextLoc*2] == 0 or timeCheck[nextLoc*2] > time +1:
                timeCheck[nextLoc*2] = time+1
                answer = 1
            continue
        timeCheck[nextLoc*2] = time+1
        queue.append([nextLoc*2,time+1])
        
if (N==K):
    print(0)
    print(1)
else:
    print(timeCheck[K]-1)
    print(answer)
