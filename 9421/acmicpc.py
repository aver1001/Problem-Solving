import sys
sys.stdin = open('input.txt', "r")

'''
양의 정수 n의 각 자리수의 제곱의 합을 계산한다
그렇게 해서 나온 합도 각 자리수의 제곱의 합을 계산한다.

'''

N = int(sys.stdin.readline().rstrip())

'''
일단 소수를 구한다

소수중에서 상근수인걸 구한다
=>  상근수 계산식을 돌리다 나왔던 수가 또 나올경우 상근수 X
    1이 나올경우 상근수
'''

primeNumber = []

check = [False]*(N+1)
for i in range(2, N+1):

    if check[i] == False:
        primeNumber.append(i)

        for j in range(i, N+1, i):
            check[j] = True


sangGen = set()
notSangGen = set()

for pnum in primeNumber:

    # 구해놓은 상근수에 들어갈경우
    if pnum in sangGen:
        print(pnum)

    # 구해놓은 상근수가 아닌수에 들어갈경우
    elif pnum in notSangGen:
        continue

    # 아직 찾아보지 못한 수 일경우
    else:
        temp = set()
        temp.add(pnum)

        nowPnum = pnum
        while True:
            nextPnum = 0
            for i in str(nowPnum):
                nextPnum += int(i)**2
                # 상근수 일경우
            if nextPnum == 1:
                # 상근수 업데이트
                sangGen.update(temp)
                print(pnum)
                break
            # 이전에 나왔던 숫자일 경우
            if nextPnum in temp:
                # 상근수 아닌거 업데이트
                notSangGen.update(temp)
                break
            temp.add(nextPnum)
            nowPnum = nextPnum
