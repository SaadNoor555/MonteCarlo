import csv
import random
import matplotlib.pyplot as plt

file = open('IIM.csv', 'r')
csvreader = csv.reader(file)
data = list(csvreader)
n = len(data)
prev_changes = []
# we are using rate of change
for i in range(2, n):
    # change = (yesterday's price - today's price) / yesterday's price
    prev_changes.append((float(data[i-1][1])-float(data[i][1]))/float(data[i-1][1]))
for sim in range(100):
    last_price = float(data[n-1][1])
    prices = []
    for i in range(30):
        last_price = last_price + last_price*random.choice(prev_changes)
        prices.append(last_price)
    # print(prices)
    x = [ i for i in range(30)]
    plt.plot(x, prices)
x = [i for i in range(30)]
y = [float(data[n-1][1]) for i in range(30)]
plt.plot(x, y, linestyle='-.')
plt.show()
file.close()
