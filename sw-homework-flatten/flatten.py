import sys
sys.stdin = ('input.txt')
##############################

T = 10

for tc in range(T):
    dump = int(input()) # 덤프 가능한 횟수
    data = list(map(int, input().split()))
    high_num = 0
    low_num = 0
    high_num_ea = 0
    low_num_ea = 0

    for nn in range(dump):
        if data[nn] > data[nn-1]:
            high_num = data[nn]
        if data[nn] < data[nn-1]:
            low_num = data[nn]
        
    for mm in data:
        if mm == high_num:
            high_num_ea += 1
        if mm == low_num:
            low_num_ea += 1

# 박주현 형님의 코드 ----------------------------------------
#Test_Case = 10
 
# for i in range(Test_Case):
 
#     dump_num = int(input())
#     box_list = list(map(int, input().split()))
 
#     for j in range(dump_num):
#         max_val = max(box_list)
#         min_val = min(box_list)
#         max_index = box_list.index(max_val)
#         min_index = box_list.index(min_val)
 
#         box_list[max_index] -= 1
#         box_list[min_index] += 1
 
#     print(f'#{i + 1} {max(box_list) - min(box_list)}')
    




# 최대값의 절대값, 최소값 절대값 구하여라, 그 갯수도 구하여라 >> 1씩 줄어, 늘어나면서
# 최대값이 0이 되는 시점에 최대값을 -1을 시키고
# 최소값이 0이 되는 시점에 최소값을 +1을 시키고
# N번 반복... 
# 그렇게 하다가 ? 마지막이 되면 최대값 - 최소값을 출력한다.