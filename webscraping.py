import bs4 as bs
import pandas as pd 
import requests 


url = 'https://bazaar.shopclues.com/appliances-led-tvs.html'

request = requests.get(url)
print(request)