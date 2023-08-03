import sys
sys.stdin = open('input.txt')
##############################

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    absum = a + b
    print(f'Case #{i+1}: {a} + {b} = {absum}')