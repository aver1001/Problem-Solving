import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

# 일단 소수의 합이기때문에
# '소수' 인지 아닌지를 알아야함.
# 입력이 1 ~ 4000000이기떄문에 이만큼의 소수를 아리뭐시기의 체로 구해줌

if N == 1:
    print(0)
    exit()

primeNumber = [False]*(N+1)
pNumList = []
for i in range(2, N+1):
    if primeNumber[i] == False:
        primeNumber[i] = True
        pNumList.append(i)
        temp = i
        while True:

            temp += i
            if temp >= N+1:
                break
            primeNumber[temp] = True


lt, rt = 0, 0
hap = pNumList[0]
answer = 0
while True:
    # 구할려는 수보다 클 경우
    if hap > N:
        # 왼쪽을 줄여준다
        hap -= pNumList[lt]
        lt += 1

    # 구할려는 수와 같을경우
    elif hap == N:
        answer += 1
        # 왼쪽을 줄여준다
        hap -= pNumList[lt]
        lt += 1
    # 구할려는 수보다 작을경우
    else:
        rt += 1
        if rt == len(pNumList):
            break
        hap += pNumList[rt]

    if lt > rt:
        break

print(answer)
