import sys
sys.stdin = open('input.txt', "r")
#사람의 이름 개수 n
#폭의 길이 m
n, m = map(int, sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(n+1)

nameLen = []
for _ in range (n):
    nameLen.append(int(sys.stdin.readline().rstrip()))
MAX_VALUE = (m**2)*n
DP = [[-1]*(m) for _ in range (n)]      # 가로=열의 총 갯수, 세로=숫자의 총갯수

#  n번째 숫자에 해당하는 별을 넣을 때에는 n-1번째의 별의 다음 행에 새로 시작할 수 있고, n-1째 별의 마지막에서 한칸 띄고 이어서 넣을 수도 있다.

def DFS(idx:int, tmp:int):
    
    if DP[idx][tmp] == -1:      #방문하지 않은 곳이라면
        if idx == n-1:          #마지막 문자라면 0을 넣어준다
            DP[idx][tmp] = 0
        else:                   #마지막 문자가 아니라면
            if tmp +1 +nameLen[idx+1] < m:     # 이번칸에 문자를 넣을수 있다면
                                    #최솟값 (이번칸에 문자를 넣는것과             무시하고 다음칸에 넣는것 + 이번에 빈칸^2)
                DP[idx][tmp] = min(DFS(idx+1,tmp+1+nameLen[idx+1]), DFS(idx+1,nameLen[idx+1]-1) + (m-tmp-1)**2)
            else:                              # 이번칸에 문자를 넣을수 없다면
                                #다음칸에넣고 이번값의 빈칸^2
                DP[idx][tmp] = DFS(idx+1,nameLen[idx+1]-1) +(m-tmp-1)**2
                
    return DP[idx][tmp]

print(DFS(0,nameLen[0]-1))
#print(cnt)