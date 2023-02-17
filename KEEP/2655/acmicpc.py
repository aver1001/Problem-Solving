import sys
sys.stdin = open('input.txt', "r")




'''
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다.
탑은 벽돌을 한 개씩 아래에서 위로 쌓으면서 만들어 간다
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램을 작성하시오.

    1. 벽돌은 회전시킬 수 없다. 즉 옆면을 밑면으로 사용할 수 없다.
    2. 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
    3. 벽돌들의 높이는 같을 수도 있다.
    4. 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
    5. 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없.
    
'''

N = int(sys.stdin.readline().rstrip())
block = [(sys.maxsize,sys.maxsize,sys.maxsize)]

DP = [[0]*(N+1) for _ in range (N+1)]
for idx in range (1,N+1):
    width,height,weight = map(int,sys.stdin.readline().rstrip().split())
    block.append((width,height,weight))
    

def DFS(v,beforeIdx):

    if DP[v][beforeIdx] != 0:
        return DP[v][beforeIdx]
    
    nowWidth, _ ,nowWeight = block[beforeIdx]
    
    ret = 0
    for idx in range (1,N+1):
        nextWidth,nextHeight,nextWeight = block[idx]
        #다음에 올릴게 넓이가 더 작고, 무게도 더 작을경우
        if nextWidth < nowWidth and nextWeight < nowWeight:
            if DP[v+1][idx] == 0:
                DP[v+1][idx] = DFS(v+1,idx)+nextHeight
            #print(nextWidth,'<',nowWidth,'AND',nextWeight,'<',nowWeight)

            ret = max(ret,DP[v+1][idx])

    DP[v][beforeIdx] = ret
    return DP[v][beforeIdx]
    
answer = []

def findAnswer(v,beforeIdx,hap):
    if hap == 0:
        return
    nowWidth, nowHeight ,nowWeight = block[beforeIdx]
    
    for nextIdx in range (1,N+1):
        if DP[v+1][nextIdx] != hap:
            continue
        nextWidth,nextHeight,nextWeight = block[nextIdx]
        if nextWidth < nowWidth and nextWeight < nowWeight and DP[v+1][nextIdx]:
            answer.append(nextIdx)
            findAnswer(v+1,nextIdx,hap-nextHeight)
            
findAnswer(0,0,DFS(0,0))
print(len(answer))
for i in reversed(answer):
    print(i)
    