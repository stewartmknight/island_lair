# import dependancies
import requests
import urllib
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time
import pandas as pd

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
        name = name.replace(".", "")
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

    # Create a dataframe
    df = pd.DataFrame({"Island_Name": names,
                    "Acreage": acres,
                    "Country": countrys})

    return(df)