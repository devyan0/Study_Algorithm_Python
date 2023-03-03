prices = [7, 1, 5, 3, 6, 4]
days = len(prices)
profit = 0

for buy in range(days):
    for sell in range(buy+1, days):
        profit = max(profit, prices[sell]-prices[buy])

print(profit)