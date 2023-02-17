import sys
import heapq
from collections import deque
sys.stdin = open('input.txt', "r")
'''
1.  NowTime을 0으로 초기화한다.
2.  빈 계산대를 heap에 넣어준다.
3.  빈 계산대가 없을때까지 heap에서 pop 해주고,
    손님의 물건의 개수 + NowTime을 넣어서 계산중heap에 넣어준다.
4.  빈 계산대가 없다면, 계산중 heap에서 하나 꺼내준뒤 현재 시각을 개수+NowTime으로 바꿔준다.
5.  계산중인 사람중에 개수+NowTime 인 사람이 있다면 다 꺼내준다.
6.  꺼내준 사람들을 계산대가 큰 순서로 정렬해서 answer += 순서 * 회원ID 해준다.
7.  계산 끝난 계산대는 다시 빈 계산대에 넣어준다.


'''

N,K = map(int, sys.stdin.readline().rstrip().split())
userList = deque([])
for _ in range (N):
    id,cnt = map(int, sys.stdin.readline().rstrip().split())
    userList.append((cnt,id))
    
#1.  NowTime을 0으로 초기화한다.
NowTime = 0
answer = 0
cnt = 1
#2.  빈 계산대를 heap에 넣어준다.
remainCal = [i for i in range (1,K+1)]
NowCal = []
EndPeople = []
#3.  빈 계산대가 없을때까지 heap에서 pop 해주고, 손님의 물건의 개수 + NowTime을 넣어서 계산중 heap에 넣어준다.
while (remainCal):
    calIdx = heapq.heappop(remainCal)
    userCnt,userId = userList.popleft()
    heapq.heappush(NowCal,(userCnt+NowTime, userId,calIdx)) # 계산 끝나는 지점의 시간, 유저의 Id, 점유중인 계산대 번호
#4.  빈 계산대가 없다면, 계산중 heap에서 하나 꺼내준뒤 현재 시각을 개수+NowTime으로 바꿔준다.
Time, userId, calIdx = heapq.heappop(NowCal)
NowTime = Time
heapq.heappush(EndPeople,(-calIdx,userId)) #-계산대 번호, 유저의 Id
#5.  계산중인 사람중에 개수+NowTime 인 사람이 있다면 다 꺼내준다.
while (True):
    if len(NowCal) == 0:
        break
    if NowCal[0][0] > NowTime:
        break
    else:
        Time, userId, calIdx = heapq.heappop(NowCal)
        heapq.heappush(EndPeople,(-calIdx,userId)) #-계산대 번호, 유저의 Id
#6.  꺼내준 사람들을 계산대가 큰 순서로 정렬해서 answer += 순서 * 회원ID 해준다.
while (EndPeople):
    calIdx,userId = heapq.heappop(EndPeople)
    answer += cnt * userId
    cnt += 1
    #7.  계산 끝난 계산대는 다시 빈 계산대에 넣어준다.
    heapq.heappush(remainCal,-calIdx)
    