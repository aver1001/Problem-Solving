import sys
sys.stdin = open('input.txt', "r")
sys.setrecursionlimit(1000000)

#사람의 이름 개수 n
#폭의 길이 m
n, m = map(int, sys.stdin.readline().rstrip().split())
nameLen = []
for _ in range (n):
    nameLen.append(int(sys.stdin.readline().rstrip()))
    
DP = [[-1]*(m+1) for _ in range (n+1)]

'''
DP를 구현해야함.

'''
cnt = 0
def DFS(v:int, remain:int, hap:int,level:int):
    global cnt
    cnt += 1
    if v == n:
        return hap
    
    print(level,remain)
    
    #이번줄에 이름을 쓸것인가
    answer = sys.maxsize
    ## 이번줄에 쓰지만 꽉 채웠기 때문에 다음줄로 넘어감
    if(remain == nameLen[v]):
       answer = min(DFS(v+1,m,hap,level+1),answer)
    ## 이번줄에 쓸경우
    elif (remain > nameLen[v]):
        answer = min(DFS(v+1,remain-nameLen[v]-1,hap,level),answer)
    
    #다음줄에 이름을 쓸것인가
    answer = min(DFS(v+1,m-nameLen[v]-1,hap+pow(remain+1,2),level+1),answer)
    return answer

print(DFS(0,m,0,0))
print(cnt)