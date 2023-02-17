import sys
sys.stdin = open('input.txt', "r")

str = sys.stdin.readline().rstrip()
N = len(str)-1

DP = [[None]*(N+1) for _ in range (N+1)]
DP2 = [i for i in range (1,N+3)]
DP2[-1] = 0
def isPel(start,end):

    if end-start <= 1:
        DP[start][end] = str[start] == str[end]
    else:
        if DP[start][end] == None:
            DP[start][end] = str[start] == str[end] and isPel(start+1,end-1)
        
    return DP[start][end]
for lt in range (N+1):
    for rt in range (lt,N+1):
        #print(lt,rt)
        if isPel(lt,rt):
            #print('!!')
            DP2[rt] = min(DP2[lt-1]+1, DP2[rt])
    #print()
print(DP2[-2])