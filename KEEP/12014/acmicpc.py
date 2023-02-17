import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

'''
1.  총 K번 주식 구매를 할 수 있으며 하루에 한번만 구매할 수 있다.
2.  주식을 살 때마다 맨 처음을 제외하고는 바로 직전에 주식을 샀을 때보다 가격이 올라갔을 때만 사기로 했다.
3.  N과 K, 주가가 주어졌을때 주어진 조건을 만족하게 주식을 구입할 수 있는지 여부를 알려주는 프로그램을 작성하시오.

해결방법
################################################################################################
결국 증가하는 수열 찾는 LCS 말하는거 같음.
'''

T = int(sys.stdin.readline())
for test_case in range (1,T+1):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    price = list(map(int, sys.stdin.readline().rstrip().split()))
    check = [price[0]]
    
    for num in price[1:]:
        
        if check[-1]< num:
            check.append(num)
        else:
            check[bisect_left(check,num)] = num
    
    print("Case #{test_case}".format(test_case = test_case))
    if len(check) >= K:
        print(1)
    else:
        print(0)

    
'''
T1
50 60 75 78 105 110 

T2
50

T3
5 10 12 13

'''