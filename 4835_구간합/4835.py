import sys
sys.stdin = open('input.txt')


T = int(input()) #테스트 케이스의 개수

for tc in range(T):
    N, M = list(map(int, input().split())) # N은 인덱션 수, M은 합할 수
    numbers = list(map(int, input().split()))
    maxsum = 0
    minsum = 1000000

    for i in range(N - M + 1):
        temp = sum(numbers[i:i+M])
        if temp > maxsum:
            maxsum = temp
        if temp < minsum:
            minsum = temp

        # 정수data를 돌려서 뽑았는데, 순서대로 3개씩 계산을 해서 제일 큰 값과 작은 값을 고르고, 빼라
    print(f'#{tc+1} {maxsum - minsum}')

