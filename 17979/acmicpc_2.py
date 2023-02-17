import sys
sys.stdin = open('input.txt', "r")

'''
[백준 17979 What’s Mine in Mine] G4
1:37 ~ 1:52 (15분 소요)

새로운 게임 “Mining Simulator”가 발매되었다. 
이 게임에서는 미네랄이 특정 시간마다 나타난다. 그리고 너는 그 미네랄이 나타났을 때 캘 수 있다.
채광이 끝난 이후, 너는 미네랄을 돈으로 바꿀 수 있다.
미네랄의 양은 ~~~
미네랄 하나하나의 가격은 사전에 정해진다.

게임에서 너는 센서를 보유한다.
그 센서는 미네랄이 그 날 언제 나타나는지 알려준다.
그리고 매일 아침, 각 타입에 대한 미네랄의 가격이 정해진다.
서로 다른 미네랄이 같은 시간에 등장했을 때 너는 하나만 캘 수 있다.

m개의 미네랄에대한 가격이 주어지고, 하루에 n개의 광석이 나타날 때, 
그 날 가장 많은 돈을 벌 수 있는 경우를 구하는 프로그램을 작성해라. 
미네랄의 양은 등장지속시간과 동일하다(end time - start time). 
너는 한가지 광물을 다 캐야 다음 채굴을 시작할 수 있다. 
(먼저 캔 광물의 end - time 과 다른 광물의 start-time은 동일할 수 있다.)= end time 과 start-time이 동일 할 때 그 광물을 캘 수 있다는 뜻.

아래 그림에서
(s, e, t) = (start time, end time, mineral type)


아래 그림을 봤을 때, 너가 만약 (2, 5, 1)광물을 캤다면 
광물의 양은 (5-2) #end time - start time = 3이 될 것이고 type이 1이므로 
3(광물의 양) * 2(타입1의 가격) = 6원을 벌게 되는 것이다.

입력:
(1) 첫 째 줄에 m, n이 주어진다.
M = 미네랄 타입의 수    1<= M <= 100
N = 광물의 등장 횟수    1<= N <= 100,000

(2) 다음 m개의 줄에 
각 타입의 가격이 주어진다.

(3) 다음 n개의 줄에
등장하는 광물의 (start time, end time, type) 이 주어진다.

이 때 이 날 벌 수 있는 돈의 최대값을 구하여라


'''

'''
시간의 최대값이 15000 임. 충분히 배열로 만들어도 괜찮음.
배열을 15000까지 만들고 
start 순서로 sort 한다음 최대값 정리?
'''

m, n = map(int, sys.stdin.readline().rstrip().split())
mCost = {}
for i in range(1, m+1):
    mCost[i] = int(sys.stdin.readline().rstrip())
mineral = []
for _ in range(n):
    start, end, type = map(int, sys.stdin.readline().rstrip().split())
    mineral.append([start, end, type])

mineral.sort(key=lambda x: x[1])


def find(start, end, type):
    global table
    if len(table) == 0:
        table = {end: (end-start)*mCost[type]}
    temp = {}
    for key, value in table.items():
        # 만약 끝나는 시간이 내 시작시간 이전일경우
        if start >= key:
            if end in table and end in temp:
                temp[end] = max(table[end], temp[end],
                                (value+(end-start)*mCost[type]))
            elif end in table:
                temp[end] = max(table[end], (value+(end-start)*mCost[type]))
            elif end in temp:
                temp[end] = max(temp[end], (value+(end-start)*mCost[type]))
            else:
                temp[end] = (value+(end-start)*mCost[type])

    table.update(temp)

    if end in table:
        table[end] = max(table[end], (end-start)*mCost[type])
    else:
        table[end] = (end-start)*mCost[type]


global table
table = dict()
for m in mineral:
    find(*m)

print(max(table.values()))
