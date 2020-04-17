import json

av_profit = {}
my_list = []
profit = {}
amount = 0
with open('qwe.txt', encoding='UTF-8') as f:
    for line in f:
        name, form, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        amount += profit[name]
    av_profit['average_profit'] = amount / len(profit.keys())
    my_list.append(profit)
    my_list.append(av_profit)
with open('qwe.json', 'x') as f:
    json.dump(my_list, f)
