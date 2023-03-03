import sys
sys.stdin = open('input.txt', "r")

postive = []
negative = []
Zero = False
N = int(sys.stdin.readline())

for _ in range (N):
    temp = int(sys.stdin.readline())
    if temp < 0:
        negative.append(temp)
    elif temp > 0:
        postive.append(temp)
    else:
        Zero = True
        
        
negative.sort(reverse=True)
postive.sort()

hap = 0

while postive:
    if len(postive) >= 2:
        if postive[-1] == 1 or postive[-2] == 1:
            hap += postive.pop() + postive.pop()
            continue
        hap += postive.pop() * postive.pop()
    elif len(postive) == 1:
        if postive[-1] == 1:
            hap += postive.pop()
            continue
        hap += postive.pop()
        
while (len(negative) >= 2):
    hap += negative.pop() * negative.pop()
    
while negative:
    if Zero:
        break
    else:
        hap += negative.pop()

print(hap)
    