import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    N = int(sys.stdin.readline().rstrip())
    fileList = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    answer = 0
    while True:
        Min = sys.maxsize
        lt, rt = None, None
        isProcess = False
        for idx in range(N):

            if fileList[idx] == None:
                continue
            if lt == None:
                lt = idx
                continue

            if rt == None:
                rt = idx

            if Min > fileList[lt] + fileList[rt]:
                Min = fileList[lt] + fileList[rt]
                target = [lt, rt]
            lt = rt
            rt = None
            isProcess = True

        if isProcess == False:
            break
        print(fileList[target[0]], fileList[target[1]])
        answer += fileList[target[0]] + fileList[target[1]]
        fileList[target[0]] = fileList[target[0]] + fileList[target[1]]
        fileList[target[1]] = None

    print(answer)
