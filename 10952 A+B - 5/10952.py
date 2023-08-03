import sys
sys.stdin = open('input.txt')
##############################

#10대신 뭐가 들어가야되나요?
#테스트케이스의 개수 횟수.

while True:
    A, B = map(int, input().split())
    if A + B == 0 :
        break
    print(A+B)