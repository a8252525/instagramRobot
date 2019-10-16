# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:33:14 2019

@author: ideapad 320
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:46:33 2019

@author: ideapad 320
"""
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
beautifultw_url='http://www.ngchina.com.cn/animals/'
res=requests.get(beautifultw_url).text
#driver=webdriver.Chrome('C:/Users/ideapad 320/.spyder-py3/chromedriver_win32/chromedriver.exe')
#driver.get(beautifultw_url)
soup=BeautifulSoup(res, 'lxml')

img_alt=soup.find_all('img',{'src':re.compile('http:.*?\.jpg')})

for link in img_alt:2
    url=link['src']
    with requests.get(url, stream=True) as r:
        image_name=url.split('/')[-1]
        with open('C:/Users/ideapad 320/Desktop/IG機器人/discovery/{}'.format(image_name),'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
    print('Saved %s' % image_name)
