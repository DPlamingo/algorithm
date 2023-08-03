import sys
sys.stdin = open('input.txt')
##############################

T = int(input())

for i in range(T):
    space = ' '
    star = '*'
    print((space * ((T-1) - i) ) + (star * (i + 1)))