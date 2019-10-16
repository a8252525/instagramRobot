# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:46:33 2019

@author: ideapad 320
"""
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
beautifultw_url='https://www.instagram.com/explore/tags/%E5%8F%B0%E7%81%A3%E7%BE%8E%E6%99%AF/?hl=zh-tw'
res=requests.get(beautifultw_url).text
soup=BeautifulSoup(res, 'lxml')

img_alt=soup.find_all('img',{'src':re.compile('http:.*?\.jpg')})
print(img_alt)
for link in img_alt:
    print(link['src'])
    

#print(img_alt)
    
    
    
driver=webdriver.Chrome('C:/Users/ideapad 320/.spyder-py3/chromedriver_win32/chromedriver.exe')
driver.get(beautifultw_url)
elem = driver.find_element_by_class_name('KL4Bh')
print(elem)