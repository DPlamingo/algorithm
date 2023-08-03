#
import sys
sys.stdin = open('input.txt')
#

T = 10 # 테스트 케이스의 개수

# 맨 왼쪽 두 칸과, 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다.
for t in range(T): # 테스트케이스를 반복하는 0~9까지 총 10번..
    N = int(input())  # 건물의 개수
    H = list(map(int, input().split()))  # N개의 건물의 높이
    build_sum = 0 # 조망권이 확보된 세대의 수

    for i in range(2, N - 2):# 연속된 건물 높이 즉, (n-2, n-1, n , n+1, n+2) 비교 했을 때, n이 제일 클 경우 +1을 해라
        if H[i - 2] < H[i] and H[i - 2] < H[i] and H[i + 1] < H[i] and H[i + 2]:
            build_sum +=

    print(f'#{t + 1} {build_sum}')