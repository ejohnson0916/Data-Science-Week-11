import pandas as pd
import requests
from bs4 import BeautifulSoup

# Import Excel file
data = pd.read_csv(filepath_or_buffer='C:/Users/eanmj/Desktop/Data/COVID19_03242020_ByCounty.csv')

# Scrape a web page
url = 'https://hackersandslackers.com/tag/dataengineering/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

match = soup.title.text
print(match)
