"""
Steven Felesky
Dillon Tartt

Scrape historical data from financial websites
"""

import re
import requests
from datetime import date, timedelta

# Get a list of dates from 2021-03-31 to 2022-03-31
# to be used to iterate through archive.org urls
dates = []
start_date = date(2022, 3, 31)
end_date = date(2022, 4, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    dates.append(start_date.strftime("%Y%m%d"))
    start_date += delta

# dictionary for headlines with k=date, v=list of headlines
mw_headlines_dict = {}

for date in dates:
    url = 'https://web.archive.org/web/' + date + '/https://www.marketwatch.com/'
    response = requests.get(url)

    # find all story(headline) links with bitcoin or crypto in them, clean and remove duplicates
    headlines = re.findall('/story/(.*(?:crypto|bitcoin).*)-.*mod=home', response.text)
    headlines = [x.replace('-',' ') for x in headlines]
    headlines = list(set(headlines))

    # add to dict
    mw_headlines_dict[date] = headlines

print(mw_headlines_dict)