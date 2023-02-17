import sys
sys.stdin = open('input.txt', "r")

N,R,G,B = map(int, sys.stdin.readline().rstrip().split())

def factorial(a):
    
    answer = 1
    for i in range (1,a+1): answer *= i
    return answer

def DFS(v,R,G,B):
    if v == N+1:
        return 1
    hap = 0
    
    #한가지 색으로 채울경우
    if R >= v:
        hap += DFS(v+1,R-v,G,B)
    if G >= v:
        hap += DFS(v+1,R,G-v,B)
    if B >= v:
        hap += DFS(v+1,R,G,B-v)
    #두가지 색으로 채울경우
    if v % 2 == 0:
        if R >= v//2 and G >= v//2:
            hap += factorial(v)//(factorial(v//2))//(factorial(v//2))*DFS(v+1,R-v//2,G-v//2,B)
        if G >= v//2 and B >= v//2:
            hap += factorial(v)//(factorial(v//2))//(factorial(v//2))*DFS(v+1,R,G-v//2,B-v//2)
        if R >= v//2 and B >= v//2:
            hap += factorial(v)//(factorial(v//2))//(factorial(v//2))*DFS(v+1,R-v//2,G,B-v//2)
    #세가지 색으로 채울경우
    if v % 3 == 0:
        if R >= v//3 and G >= v//3 and B >= v//3:
            hap += factorial(v)//(factorial(v//3))//(factorial(v//3))//(factorial(v//3))*DFS(v+1,R-v//3,G-v//3,B-v//3)
    return hap

            
print(DFS(1,R,G,B))