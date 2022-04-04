# NLP Bitcoin Price Prediction

Steven Felesky

Dillon Tartt

CSCI 334 - Spring 2022

## How to run
We recommend setting up a virtual python environment (with venv for example)

1. Install required packages

        pip install nltk requests

2. Run utils_scrape.py to get data OR run with data from data directory

        python utils_scrape.py

3. Run utils_btc_vel.py to determine if bitcoin went up or down OR use data in data directory

        python utils_btc_vel.py

4. Run utils_sent_analysis.py to determine sentiment on bitcoin for each day in mw_headlines.csv

        python utils_sent_analysis.py

5. Use the output of utils_sent_analysis.py to predict the output of utils_btc_vel.py (We used weka to train and run a random-forest model with 57% accuracy)


### Other notes
A precompiled dataset with the date, sentiment score and btc price is included in the data directory. (mw_sent_btc_vel.csv)

### Future work
Based on other work we believe we can increase the accuracy of this model by tweaking the way we do sentiment analysis. The nltk precompiled sentiment analysis model (VADER) was used to save time and complete the proof of concept, but further tweaking in this area can be done.
