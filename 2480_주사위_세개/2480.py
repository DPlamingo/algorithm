import sys
sys.stdin = open('input.txt')
##############################

a, b, c = map(int, input().split())
# a - 첫번째 값
# b - 두번째 값
# c - 세번째 값

if a == b == c :
    print((a * 1000) + 10000)

elif a == b or b == c or c == a :
    if a == b :
        print((a * 100) + 1000)
    elif b == c :
        print((b * 100) + 1000)
    elif c == a :
        print((c * 100) + 1000)
        
elif a != b and b != c and c != a:
    if a > b and a > c:
        print(a*100)
    elif b > a and b > c:
        print(b*100)
    else :
        print(c*100)