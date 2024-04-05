import random
# parameter : n
# return : list
# 1~45 사이의 서로 다른 번호를 무작위로 n개 뽑고 그 번호들이 담긴 리스트를 리턴
def generate_numbers(n):
    number_list = []
    count = 0
    while count < n:
        num = random.randint(1, 45)
        if num in number_list:
            continue
        else:
            number_list.append(num)
            count += 1

    return number_list

# return : list
# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴
# 일반 당첨 번호 6개는 정렬, 보너스 번호는 마지막에 추가
def draw_winning_numbers():
    winning_numbers = generate_numbers(6)
    while True:
        bonus_num = generate_numbers(1)
        if bonus_num not in winning_numbers:
            break
    winning_numbers.sort()
    winning_numbers = winning_numbers + bonus_num
    return winning_numbers


# parameter : list_1, list_2
# return : int
# 두 리스트 사이에 겹치는 번호의 개수를 리턴
def count_matching_numbers(numbers, winning_numbers):
    return len(numbers) + len(winning_numbers) - len(set(numbers + winning_numbers))

# parameter : list_1, list_2
# return : int
# 당첨 금액을 리턴
def check(numbers, winning_numbers):
    check_bonus = False
    if winning_numbers[-1] in numbers:
        check_bonus = True
    if count_matching_numbers(numbers, winning_numbers) == 6 and not check_bonus:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 6 and check_bonus:
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers) == 5 and not check_bonus:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4 and not check_bonus:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3 and not check_bonus:
        return 5000
    else:
        return 0

