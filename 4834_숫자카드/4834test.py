# import sys
# sys.stdin = ('input.txt')

Test_case = int(input())

for test_case in range(Test_case):
    num_of_card = int(input())
    card_list_str = input()
    card_list = []

    for char in card_list_str:
        card_list.append(int(char))

    print(card_list)

    card_dict = {}
    