import random

max_chance = 4
chance_count = 4

answer = random.randint(1, 20)

while chance_count > 0:
    guess_num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(chance_count)))
    if answer == guess_num:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(max_chance - chance_count + 1))
        break
    elif answer > guess_num:
        print("Up")
        chance_count -= 1
    else:
        print("Down")
        chance_count -= 1

if chance_count == 0:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))