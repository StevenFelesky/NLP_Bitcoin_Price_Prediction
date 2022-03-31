"""
Steven Felesky
Dillon Tartt

Scrape historical data from financial websites
"""

import requests
import re

res = requests.get('https://web.archive.org/web/20210331/https://www.marketwatch.com/')
[res.text for m in re.finditer('test', 'test test test test')]
print(res.text)