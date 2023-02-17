import sys
sys.stdin = open('input.txt', "r")

num = list(sys.stdin.readline().rstrip())
usenum = ''
answer = [0] * 10
N = len(num)
cnt = 1
while num:
    temp = num.pop()
    usenum = temp + usenum
    temp = int(temp)

    if len(num) == 0:
        break
    times = int(''.join(num))
    # 0~9까지 num에 남아있는 숫자만큼 반복되었을 것
    for idx in range(10):
        answer[idx] += times

    for idx in range(1, temp):
        answer[idx] += int(usenum)
        
    answer[temp] += 

    cnt *= 10
print(answer)
