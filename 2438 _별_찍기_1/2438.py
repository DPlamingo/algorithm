import sys
sys.stdin = open('input.txt')
##############################

T = int(input())

for i in range(T):
    star = '*'
    print(star * (i+1))