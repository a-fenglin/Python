import requests

import re
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver

#爬取地址
url = 'http://111.198.29.45:48594/'
r = requests.get(url)
r.encoding = 'gb2312'

# 利用 re 
matchs = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", r.text)
for link in matchs:
    print(link)

print()

# 利用 BeautifulSoup4 （DOM树）
soup = BeautifulSoup(r.text, 'lxml')
for a in soup.find_all('a'):
    link = a['href']
    print(link)

print()

# 利用 lxml.etree （XPath）
tree = etree.HTML(r.text)
for link in tree.xpath("//@href"):
    print(link)

print()

# 利用selenium
driver = webdriver.Firefox()
driver.get(url)
for link in driver.find_elements_by_tag_name("a"):
    print(link.get_attribute("href"))
driver.close()
