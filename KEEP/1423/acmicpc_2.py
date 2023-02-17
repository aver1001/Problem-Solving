import sys
sys.stdin = open('input.txt', "r")
N = int(sys.stdin.readline())

Number = []
Power = []

line = sys.stdin.readline()

for chr in line.split():
    Number.append(int(chr))

line = sys.stdin.readline()

for chr in line.split():
    Power.append(int(chr))

D = int(sys.stdin.readline())
basic = 0

for i in range(N):
    basic += Number[i] * Power[i]

T = [0] * (D+1)

for i in range(N):                            # Level
    for _ in range(min(D, Number[i])):      # each monkey
        for idx in range(D, -1, -1):
            for day in range(1, N):
                if i + day >= N:
                    break
                if idx + day > D:
                    break
                
                T[idx+day] = max(T[idx+day], T[idx] + (Power[i+day] - Power[i]))
        print(T)

result = 0


for day in range(D+1):
    if result < T[day]:
        result = T[day]
print(T,basic)
print(result + basic)
