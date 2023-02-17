import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range (N):
    A,B = map(int, sys.stdin.readline().rstrip().split(' '))
    numbers.append((A,B))
numbers.sort(key= lambda x:x[1])
# 넣은자리를 체크해서 그 위치 기반으로 가능한 수열을 찾자
DP = [0]*N
DP[0] = 1

arr = [numbers[0]]
for idx in range(1, N):

    # 제일 마지막 숫자보다 작다면
    if numbers[idx] <= arr[-1]:
        # 자신의 위치를 찾아서 그자리에 넣어준다.
        loc = bisect_left(arr, numbers[idx])
        arr[loc] = numbers[idx]
        # 추적하기위해 DP 선언해주고 넣은 자리 체킹
        DP[idx] = loc+1
    else:
        arr.append(numbers[idx])
        # 추적하기위해 DP 선언해주고 넣은 자리 체킹
        DP[idx] = len(arr)

check = len(arr)
answer = set()
# 뒤에서 부터 찾아가면서 4..3..2..1 이런 순서로 찾아주면 된다.
for idx in range(N-1, -1, -1):
    if DP[idx] == check:
        answer.add(numbers[idx])
        check -= 1
print(N - len(answer))
t = []
for s,e in numbers:
    if (s,e) in answer:
        continue
    else:
        t.append(s)
t.sort()
for i in t:
    print(i)