#Scraping website and store in csv file
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
r = requests.get('https://its-puneet.github.io/Puneet-Singh_Portfolio/')

soup = BeautifulSoup(r.text, 'lxml')

f = csv.writer(open(' Dataprocessing.csv ','w'))
f.writerow(['Title'])
f.writerow([soup.title.text])
