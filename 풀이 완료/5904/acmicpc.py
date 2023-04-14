import sys
sys.stdin = open('input.txt', "r")

N = int(input())

def moo(acc, cur, N):
    #왼쪽과 오른쪽의 크기
    prev = (acc-cur)//2
    #만약 왼쪽에 위치한다면
    if N <= prev:
        return moo(prev, cur-1, N)
    #만약 오른쪽에 위치한다면
    elif N > prev+cur: 
        return moo(prev, cur-1, N-prev-cur)
    #자기자리 그대로라면
    else: 
        if N-prev-1:
            return "o" 
        else :
            return "m"

acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc*2+n+3
print(moo(acc, n+3, N))