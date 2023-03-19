import sys
sys.stdin = open('input.txt', "r")

def factorial(num):
    answer = 1
    for i in range (2,num+1):
        answer *= i
    return answer

def solution(n:int,l:int,r:int)-> int:
    #TODO 불가능한 조건은 다시좀 생각해보자.
        #N+1-L 보다 작고 
    #첫 막대는 그냥 설치한다.
    n -= 1
    l -= 1
    r -= 1
    answer = 1
    
    flag = False
    while (True):
        if l == r == 0:
            break
        #양쪽다 설치가 가능할 경우
        if l >= 1 and r >= 1:
            answer *= n
            l -= 1
            r -= 1
            
        #한쪽만 설치가 가능할 경우
        else:
            if l >= 1:
                l -= 1
            else:
                r -= 1
            flag = True
                
        n -= 1
        
    if flag == False:
        return 0
    return answer * factorial(n)
    

T = int(sys.stdin.readline().rstrip())
for test_case in range (T):
    
    n, l, r = map(int, sys.stdin.readline().rstrip().split())
    print(solution(n,l,r))
