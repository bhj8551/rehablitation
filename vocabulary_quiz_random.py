import random

with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    vocab_dict = {}
    vocab_count = 0
    for line in f:
        vocab_count += 1
        data = line.strip().split(': ')
        vocab_dict[vocab_count] = data
        
    while True:
        random_question = vocab_dict[random.randint(1, vocab_count)]
        question, answer = random_question[1], random_question[0]
        my_answer = input("{}: ".format(question))
        if my_answer == 'q':
            break
        elif my_answer == answer:
            print("맞았습니다!\n")
        else:
            print("틀렸습니다. 정답은 {}입니다.\n".format(answer))
    