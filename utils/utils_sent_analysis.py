"""
Steven Felesky
Dillon Tartt
 
Predict the price of bitcoin based on sentiment of headlines
"""

import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# read csv file in 
file = open('../data/mw_headlines.csv')
csvreader = csv.reader(file)
data_mw = []
for row in csvreader:
    data_mw.append(row)
file.close()

file = open('../data/bb_headlines.csv')
csvreader1 = csv.reader(file)
data_bb = []
for row in csvreader1:
    data_bb.append(row)
file.close()

scores_mw = []

# sentiment analysis market watch
sia = SentimentIntensityAnalyzer()
for row in data_mw:
    score = 0
    if len(row) > 1:
        i = 1
        while (i < len(row)):
            ps = sia.polarity_scores(row[i])
            score = score + ps['compound']
            i += 1
    scores_mw.append([row[0], score])

with open('../data/mw_headline_scores.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scores_mw)

scores_bb = []

# sentiment analysis bloomberg
for row in data_bb:
    score = 0
    if len(row) > 1:
        i = 1
        while (i < len(row)):
            ps = sia.polarity_scores(row[i])
            score = score + ps['compound']
            i += 1
    scores_bb.append([row[0], score])

with open('../data/bb_headline_scores.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scores_bb)