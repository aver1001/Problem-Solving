import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline())

DP = [-1]*(N+3)

answer = 0

def dfs(n:int,length:int,Buffer:int):
    global answer 
    
    if n >= N:
        if n == N:
            answer = max(answer,length)
        return
    
    # 화면에 A를 출력한다.
    if DP[n+1] <= length+1:
        DP[n+1] = length+1
        dfs(n+1,length+1,Buffer)
    # Ctrl-A: 화면을 전체 선택한다
    # Ctrl-C 전체 선택한 내용을 버퍼에 복사한다
    # Ctrl-V: 버퍼가 비어있지 않은 경우에는 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣는다.
    if DP[n+3] <= length+length:
        DP[n+3] = length+length
        dfs(n+3,length+length,length)
    
    if DP[n+1] <= length+Buffer:
        DP[n+1] = length+Buffer
        dfs(n+1,length+Buffer,Buffer)
        
    if DP[n+2] <= length+Buffer+Buffer:
        DP[n+2] = length+Buffer+Buffer
        dfs(n+2,length+Buffer+Buffer,Buffer)
        
dfs(0,0,0)
print(answer)
print(DP)
print(DP[N])