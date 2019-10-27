# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:36:54 2019

@author: ideapad 320
"""
ig_name=['visitgastein','lauterbrunnen','lovely_earthshotz','the.planetearth','cameraismyeye','norway.raw','earthhotspots','hribovc','naturelover_gr','teklatravel']


for i in range(3,len(ig_name)):
    try:
        s = 'posts_full -u '+ig_name[i]+' -n 200 --fetch_comments  --fetch_likes_plays --fetch_hashtags -o ./'+str(i)+'.json'
        print(s)
        runfile('C:/Users/ideapad 320/Desktop/IG機器人/instragram-crawler/instagram-crawler/crawler.py', wdir='C:/Users/ideapad 320/Desktop/IG機器人',args=s)
    except:
        pass