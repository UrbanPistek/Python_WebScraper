from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
from torrequest import TorRequest

### TOR Requests ###
password = ''
tr=TorRequest(password=password)

### Web Scrapping Rules
'''
https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/
'''

# PATH  = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
#
# #Start a driver to retrieve a Specific website
# driver.get("")
#
# '''
# All website being scraped
# '''
# attaboticsURL = "https://jobs.lever.co/attabotics"
#
# # open up connection and grabbing page
# uClient = uReq(attaboticsURL)
# page_html = uClient.read()
# uClient.close()
#
# # html parsing
# parsed_html = soup(page_html, "html.parser")

response= requests.get('http://ipecho.net/plain')
print ("My Original IP Address:",response.text)