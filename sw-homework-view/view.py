# import sys
# sys.stdin = ('input.txt')
##############################

T = 10

for tc in range(T):
    n = int(input()) # 건물의 개수
    data = list(map(int, input().split())) # 건물의 높이 100개의 데이터가 들어잇음.
    result = 0

    for dt in range(2, len(data) - 2):
        if data[dt] > data[dt - 2]:
            if data[dt] > data[dt - 1]:
                if data[dt] > data[dt + 1]:
                    if data[dt] > data[dt + 2]:

                        house = data[dt] - max(data[dt-2], data[dt-1], data[dt+1], data[dt+2])
                        result += house
    
    print(f'#{tc+1} {result}')