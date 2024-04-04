with open('chicken.txt', 'r', encoding='utf-8') as f:
    count = 0
    sum_sales = 0
    for line in f:
        sales = int(line.strip().split()[1])
        sum_sales += sales
        count += 1

print(sum_sales / count)
