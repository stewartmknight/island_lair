# import dependancies
import requests
import urllib
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time
import scrape
import pandas as pd


# Initiate Browser instance
executable_path = {"executable_path":"chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://www.privateislandsonline.com/search?region=&diversion=&availability=sale&price_range=0%3A50000000&size_range=0%3A1000&q=&view%5B%5D=1&type%5Bprivate_island%5D=1&lifestyles%5Blarge_acreage%5D=1&lifestyles%5Bocean_island%5D=1&order=price_usd%3ADESC&order=price_usd%3ADESC&type%5Bprivate_island%5D=1"
browser.visit(url)

y = 0
while y > -1:
    y = y + 100
    browser.execute_script("window.scrollTo(0, " + str(y) + ")")
    time.sleep(.4)
    max_height = browser.execute_script("return document.body.scrollHeight")
    current_height = browser.execute_script("return window.pageYOffset;")

    difference = max_height-current_height
    print(difference)
    if difference < 700:
        print("break")
        break

df = scrape.scrape(browser)

df.to_csv("island_info.csv", index=False)