import sys
# sys.stdin = open('input.txt')
##############################

T = int(sys.stdin.readline())

# 테스트 케이스는 행을 뜻한다.
# 여러개 데이터를 가로줄로 입력을 받으려면 포문 안에 넣어야 된다.
for i in range(T):
    fast = list(map(int, sys.stdin.readline().split()))
    A = fast[0]
    B = fast[1]
    print(A + B)