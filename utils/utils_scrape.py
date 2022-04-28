"""
Steven Felesky
Dillon Tartt

Scrape historical data from financial websites
"""

import re
import csv
import requests
from datetime import date, timedelta

# Get a list of dates from 2021-03-31 to 2022-03-31
# to be used to iterate through archive.org urls
dates = []
start_date = date(2021, 3, 31)
end_date = date(2022, 3, 31)
delta = timedelta(days=1)
while start_date <= end_date:
    dates.append(start_date.strftime("%Y%m%d"))
    start_date += delta

# array of array of headlines
mw_headlines = []
bb_headlines = []

for date in dates:
    url_mw = 'https://web.archive.org/web/' + date + '/https://www.marketwatch.com/'
    response_mw = requests.get(url_mw)

    # find all story(headline) links with bitcoin or crypto in them, clean and remove duplicates
    headlines_mw = re.findall('/story/(.*(?:crypto|bitcoin).*)-.*mod=home', response_mw.text)
    headlines_mw = [x.replace('-',' ') for x in headlines_mw]
    headlines_mw = list(set(headlines_mw))

    # add to headlines array
    headlines_mw.insert(0, date)
    mw_headlines.append(headlines_mw)

    ############### bloomberg
    url_bb = 'https://web.archive.org/web/' + date + '/https://www.bloomberg.com/'
    response_bb = requests.get(url_bb)

    # find all story(headline) links with bitcoin or crypto in them, clean and remove duplicates
    headlines_bb = re.findall('/news/articles/.*/(.*(?:crypto|bitcoin).*)\?', response_bb.text)
    headlines_bb = [x.replace('-',' ') for x in headlines_bb]
    headlines_bb = list(set(headlines_bb))

    # add to headlines array
    headlines_bb.insert(0, date)
    bb_headlines.append(headlines_bb)

    print(date)

with open('../data/mw_headlines.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(mw_headlines)

with open('../data/bb_headlines.csv', 'w', encoding='UTF8', newline='') as g:
    writer1 = csv.writer(g)
    writer1.writerows(bb_headlines)