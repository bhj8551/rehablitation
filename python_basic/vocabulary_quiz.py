with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        answer, question = line.strip().split(':')
        my_answer = input("{}: ".format(question))
        if my_answer == answer:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(answer))
        