# import dependancies
import requests
import urllib
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time
import pandas as pd

# Initiate Browser instance
#executable_path = {"executable_path":"chromedriver.exe"}
#browser = Browser("chrome", **executable_path, headless=False)

# Visit the url
#url = "https://www.privateislandsonline.com/search?region=&diversion=&availability=sale&price_range=0%3A50000000&size_range=0%3A1000&q=&view%5B%5D=1&type%5Bprivate_island%5D=1&lifestyles%5Blarge_acreage%5D=1&lifestyles%5Bocean_island%5D=1&order=price_usd%3ADESC&order=price_usd%3ADESC&type%5Bprivate_island%5D=1"
#browser.visit(url)
def scrape(browser):
    # Set up SOUP object
    html = browser.html
    soup = bs(html, "html.parser")

    # Find all island by loopiing through grid object in soup
    names = []
    acres = []
    countrys = []
    for grid in soup.find_all(attrs={'class': 'grid-content island-content'}):
        # Get the name
        name = grid.find(attrs={'class': 'name'}).text.strip()
        names.append(name)

        # Get the acreage
        try:
            acre = grid.find(attrs={'class': 'num'}).text.strip()
            acres.append(int(acre))
        except Exception:
            acres.append(0)

        # get the location
        for thing in grid.find_all(attrs={'class': 'list-name'}):
            try:
                location = thing.find_all('a')
                country = location[-2].text
                countrys.append(country)
            except Exception:
                countrys.append("NA")

    print(names)
    print(acres)
    print(countrys)
    
    df = pd.DataFrame({"Island_Name": names,
                    "Acreage": acres,
                    "Country": countrys})

    return(df)
