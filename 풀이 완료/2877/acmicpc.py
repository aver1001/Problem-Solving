import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(4)
    exit()
if N == 2:
    print(7)
    exit()
'''
4 2
7 3
2^0 기준으로 위아래
<2>

44 4
47 5
74 6
77 7

 2^1 기준으로 위아래
<4>
######################
444 1
447 2

474 3
477 4

744 5
747 6

774 7 
777 8

 2^2 기준으로 위아래
<8>
########################
4444
4447

4474
4477

4744
4747

4774
4777

7444
7447
'''
a = 2
temp = []
for i in range(2, 999999):
    if a >= N:
        break
    temp.append(a)
    a = a + 2**i


N = N-temp[-1]-1
answer = ''
for idx in range(i-2, -1, -1):
    if N >= 2**idx:
        answer = answer + '7'
    else:
        answer = answer + '4'

    N = N % (2**idx)

print(answer)
