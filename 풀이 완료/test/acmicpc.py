# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.stdin = open('input.txt', "r")
'''
2명이 짝지어 게임을 한다.
가위바위보 이기면 1개 가져오고 지면 1개 빼앗기고 무승부는 가만히
게임은 K번 진행하거나, 한명이 구슬을 다 잃을경우 종료

구름이와 상대방중 한명이 구슬을 모두 잃는 경우의 수를 출력하세요

구름이 구슬개수, 상대방 구슬개수, K
'''
case = 0
N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

DP = {}
for i in range(N+M+1):
    DP[(i, N+M-i)] = [0]*(K+1)
DP[(N, M)][0] = 1

for k in range(K):
    for i in range(1, N+M):
        n = i
        m = N+M-i

        for dn, dm in ((1, -1), (0, 0), (-1, 1)):
            tn = n + dn
            tm = m + dm
            if 0 <= tn <= N+M and 0 <= tm <= N+M:
                DP[(tn, tm)][k+1] += DP[(n, m)][k] % 100_000_007


print((sum(DP[(0, N+M)]) % 100_000_007+sum(DP[(N+M, 0)]) %
      100_000_007) % 100_000_007)
