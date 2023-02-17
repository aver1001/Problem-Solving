import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split(' '))
DP = {}


def solution(walkTime, WalkMoney, bicycleTime,  bicycleMoney):

    if len(DP) == 0:
        # 걸어온 시간 값 업데이트
        if walkTime in DP:
            DP[walkTime] = max(DP[walkTime], WalkMoney)
        else:
            DP[walkTime] = WalkMoney

        # 자전거 시간 값 업데이트
        if bicycleTime in DP:
            DP[bicycleTime] = max(DP[bicycleTime], bicycleMoney)
        else:
            DP[bicycleTime] = bicycleMoney

        return DP

    # 원래 있던거에서 추가해주기
    temp = {}

    for Time, Money in DP.items():

        if walkTime+Time <= K:
            if walkTime+Time in temp:
                temp[walkTime +
                     Time] = max(temp[walkTime+Time], Money+WalkMoney)
            else:
                temp[walkTime+Time] = Money+WalkMoney

        if bicycleTime+Time <= K:
            if bicycleTime + Time in temp:
                temp[bicycleTime+Time] = max(temp[bicycleTime+Time],
                                             Money+bicycleMoney)
            else:
                temp[bicycleTime+Time] = Money+bicycleMoney

    return temp


for _ in range(N):
    DP = solution(*map(int, sys.stdin.readline().rstrip().split(' ')))

print(max(DP.values()))
