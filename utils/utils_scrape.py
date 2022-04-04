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

for date in dates:
    url = 'https://web.archive.org/web/' + date + '/https://www.marketwatch.com/'
    response = requests.get(url)

    # find all story(headline) links with bitcoin or crypto in them, clean and remove duplicates
    headlines = re.findall('/story/(.*(?:crypto|bitcoin).*)-.*mod=home', response.text)
    headlines = [x.replace('-',' ') for x in headlines]
    headlines = list(set(headlines))

    # add to headlines array
    headlines.insert(0, date)
    mw_headlines.append(headlines)

    print(date)

with open('../data/mw_headlines.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(mw_headlines)