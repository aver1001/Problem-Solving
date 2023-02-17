import sys
sys.stdin = open('input.txt', "r")


table = {}
str = sys.stdin.readline().rstrip().upper()
for i in  str:
    if i in table:
        table[i] += 1
    else:
        table[i] = 1

print(table)
v = list(table.values())
k = list(table.keys())
if v.count(max(v)) != 1:
    print('?')
else:
    for key,value in table.items():
        if value == max(v):
            print(key)
            exit()