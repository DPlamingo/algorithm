import sys
sys.stdin = open('input.txt')
##############################

T = int(input())
result = 0
nums = list(map(int, input().split()))
V = int(input())

for i in range(T):

    if nums[i] == V :
        result += 1

print(result)
