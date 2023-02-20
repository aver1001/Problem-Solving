import sys
sys.stdin = open('input.txt', "r")
paper = [0]
for _ in range (6):
    paper.append(int(sys.stdin.readline()))

answer = 0
while True:
    newPaper = 36
    flag = True
    for idx in range(6,0,-1):
        print(idx)
        if paper[idx] == 0:
            continue
        
        while True:
            if (idx**2 <= newPaper and paper[idx] >0):
                flag = False
                newPaper -= (idx**2)
                paper[idx] -= 1
            else:
                break
    
    if flag:
        break
    else:
        answer += 1
print(answer)