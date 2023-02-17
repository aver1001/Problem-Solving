import time

FiboCnt = 0


def Fibo(target):

    global FiboCnt
    FiboCnt += 1

    if target == 1:
        return 0
    elif target == 2:
        return 1
    else:
        return Fibo(target-1) + Fibo(target-2)


DP = [-1]*1000
DP[1] = 0
DP[2] = 1
FiboDPCnt = 0


def FiboDP(target):
    global FiboDPCnt
    FiboDPCnt += 1
    if DP[target] != -1:
        return DP[target]
    else:
        DP[target] = FiboDP(target-1) + FiboDP(target-2)
        return DP[target]


print(Fibo(50), FiboCnt)
print(FiboDP(50), FiboDPCnt)
