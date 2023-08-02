import sys
sys.stdin = open('input.txt')
##############################

# T = 10

for x in range(10):
    jj = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0 # 0으로 해도 되는 이유 = 음수가 없기때문.. 

    #행의 합
    for i in range(100):
        tmp = 0 # i 행의 합

        for j in range(100):
            tmp += arr[i][j]

        if max_v < tmp:
            max_v = tmp

    #열의 합
    for j in range(100):
        tmp = 0 # j 행의 합

        for i in range(100):
            tmp += arr[i][j]
        
        if max_v < tmp:
            max_v = tmp

    #오른쪽아래 대각선의 합
    tmp = 0
    for i in range(100):
        tmp += arr[i][j]
    if max_v < tmp :
        max_v = tmp

    #왼쪽아래 대각선의 합
    tmp = 0
    for i in range(100):
        tmp += arr[i][99-i]
    if max_v < tmp :
        max_v = tmp

    print(f'#{x+1} {max_v}')
    