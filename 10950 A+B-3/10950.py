import sys
sys.stdin = open('input.txt')
##############################

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    a = nums[0]
    b = nums[1]
    print(a + b)