import sys
sys.stdin = open('input.txt')
##############################

T = int(input())
absum = 0
for i in range(T):
    AB = list(map(int, input().split()))
    absum = (AB[0] + AB[1])
    print(f'Case #{i+1}: {absum}')