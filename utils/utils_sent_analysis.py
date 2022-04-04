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
data = []
for row in csvreader:
    data.append(row)
file.close()

scores = []

# sentiment analysis
sia = SentimentIntensityAnalyzer()
for row in data:
    score = 0
    if len(row) > 1:
        i = 1
        while (i < len(row)):
            ps = sia.polarity_scores(row[i])
            score = score + ps['compound']
            i += 1
    scores.append([row[0], score])

with open('../data/mw_headline_scores.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scores)

