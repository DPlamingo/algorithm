import sys
sys.stdin = open('input.txt')
##############################


total_price_X = int(input())
kind_of_product_N = int(input())

howmuch = 0
for i in range(kind_of_product_N):
    product_list = list(map(int, input().split()))
    howmuch += product_list[0] * product_list[1]

if total_price_X == howmuch:
    print('Yes')
else :
    print('No')