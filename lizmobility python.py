import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# Set up Alpha Vantage API key
api_key = 'YOUR_API_KEY'
ts = TimeSeries(key=api_key, output_format='pandas')

# Get Canoo's overview and financials
data, metadata = ts.get_daily('GOEV')

latest_date = data.index[-1]
latest_data = data.loc[latest_date]

print('Open:', latest_data['1. open'])
print('High:', latest_data['2. high'])
print('Low:', latest_data['3. low'])
print('Close:', latest_data['4. close'])
print('Volume:', latest_data['5. volume'])


import yfinance as yf
import csv

# Fetch overview information for Canoo stock
canoo_stock = yf.Ticker("GOEV")
canoo_info = canoo_stock.info

# Save overview information to a CSV file
with open("canoo_overview.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Attribute", "Value"])
    for key, value in canoo_info.items():
        writer.writerow([key, value])

# Fetch overview information for Canoo stock
canoo_stock = yf.Ticker("GOEV")
canoo_info = canoo_stock.info

# Save overview information to a CSV file
with open("canoo_overview.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Attribute", "Value"])
    for key, value in canoo_info.items():
        writer.writerow([key, value])

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the element containing industry information
        industry_div = soup.find('div', class_='industry-info')
        if industry_div:
            # Extract text and split it into lines
            industry_info = industry_div.get_text(strip=True, separator='\n')
            return industry_info.split('\n')
        else:
            print("Industry information not found on the webpage.")
            return None

# URL of the webpage containing industry information
url = 'https://www.google.com/search?q=Canoo+industry'

# Get industry information
industry_info = scrape_website(url)

if industry_info:
    # Save industry information to a CSV file
    with open("industry_info.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(industry_info)

# Write the industry information to a CSV file
with open('canoo_info.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Task', 'Information']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Analyze Canoo's main competitors
    # Use the Finviz API to get a list of competitors
    url = 'https://finviz.com/screener.ashx'
    params = {
        'v': '153',
        't': 'all',
        's': 'ta_marketcap,industry,sh_avgvol_o_3m',
        'o': 'marketcap',
        'c': '2,1145,2125,2135,2145,2150,2160,2175,2200,2225,2250,2300,2350,2400,2500,3000,5000,10000',
        'p': 'sec_industry_group',
        'f': 'sec_industry_group,sh_avgvol'
        }