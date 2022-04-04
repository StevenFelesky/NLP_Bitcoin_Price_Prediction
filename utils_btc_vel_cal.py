"""
Steven Felesky
Dillon Tartt

Determine if price of btc rose or fell based on open and close prices from yahoo finance
"""

import csv

# read csv file in 
file = open('BTC-USD.csv')
csvreader = csv.reader(file)
data = []
for row in csvreader:
    data.append(row)
file.close()

data.pop(0)

up_down = []
for row in data:
    if (float(row[4]) - float(row[1])) > 1:
        up_down.append(['up'])
    else:
        up_down.append(['down'])

with open('btc_up_down.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(up_down)

