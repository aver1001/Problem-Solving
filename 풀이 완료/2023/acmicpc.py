from calendar import c
import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

primeNumber = set()
check = [False] * 100000000

for i in range(2, 100000000):
    if check[i] == False:
        primeNumber.add(i)

        for j in range(i, 100000000, i):
            check[j] = True

print(primeNumber)


# 1의자리에 올 수 있는건 2,3,5,7
