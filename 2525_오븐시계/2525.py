import sys
sys.stdin = open('input.txt')
##############################
hahaha
time, minute = map(int, input().split())
cooktime = int(input())
result = ((time * 60) + (minute + cooktime))

time = result // 60
minute = result % 60

if result // 60 >= 24:
    time -= 24

print(time, minute)
