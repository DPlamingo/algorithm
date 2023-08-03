import sys
sys.stdin = ('input.txt')
##############################

# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
#  카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

testcase = int(input())

for tt in range(testcase):
    numbers = int(input()) # 5 카드 장 수
    data = list(map(int, input( ).split()))


    for dt in data:

        


    # (numbers)장 중에 제일 많이 들어있는 값을 찾아야 한다. 어떻게?
    # 한개씩 꺼내서 순회하는 프로그램을 통해서... 조건도 달 수 있음..
    # 음... 오름차순 정렬을 한 다음.. 순서대로 가다가 음..
