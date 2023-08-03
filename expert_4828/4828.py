import sys
sys.stdin = open('input.txt')

T = int(input())

for q in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = sorted(nums)

    for i in nums:
        max_num = nums[-1:-(M+1):-1]
        min_num = nums[0:M]
        sum_max_num = 0
        sum_min_num = 0

        for num in max_num:
            sum_max_num += num

        for snum in min_num:
            sum_min_num += snum
        result = sum_max_num - sum_min_num

    print(f'#{q+1} {result}')
# 오름차순으로 정렬한 후, 맨 오른쪽 M개를 더한 값 - 맨 왼쪽 M개를 더한 값을 출력
