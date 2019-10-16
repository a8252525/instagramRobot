# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:34:35 2019

@author: ideapad 320
"""
import re
import request

n=100
with open ('C:/Users/ideapad 320/Desktop/IG機器人/instragram-crawler/instagram-crawler/output.txt','r',encoding="utf-8") as data:
    for i in range(n):
        pattern=re.complie(r'')
        img_url=re.findall('key',{'img_url'})
        
        for link in img_alt:
            url=link['src']
            with requests.get(url, stream=True) as r:
                image_name=url.split('/')[-1]
                with open('C:/Users/ideapad 320/Desktop/IG機器人/data/{}'.format(image_name),'wb') as f:
                    for chunk in r.iter_content(chunk_size=128):
                        f.write(chunk)
            print('Saved %s' % image_name)
        