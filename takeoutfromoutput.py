# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:34:35 2019

@author: ideapad 320
"""
import requests
import json

n=100
count=0
with open ('C:/Users/ideapad 320/Desktop/IG機器人/instragram-crawler/instagram-crawler/output.json','r',encoding="utf-8") as data:
    data_load = json.load(data)
    for post in data_load:
        with requests.get(post['img_url'], stream=True) as r:            
            with open('C:/Users/ideapad 320/Desktop/IG機器人/data/{}.jpg'.format(count),'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
        count+=1
        print('Saved %s' % count)
        