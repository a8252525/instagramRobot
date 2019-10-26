# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:08:50 2019

@author: ideapad 320
"""
import json
import requests

number_fans=[13600,93700,60000,44000,777000,133000,150000,54700,136000]
data_tmp=None
count=0
size=200
for i in range(1):
    #with open('test.json','r',encoding="utf-8") as data:
    with open('C:/Users/ideapad 320/Desktop/IG機器人/{}.json'.format(i),'r',encoding="utf-8") as data:
        data_load=json.load(data)
        for post in data_load:
            url=''.join(post['img_urls'][0].split('\n'))
            with requests.get(url, stream=True) as r:
                if (count%size)<170:
                    try:
                        post.update({'fans_number':number_fans[i],'comment_number':len(data_load[count]['comments']),'location':'train/{}.jpg'.format(count)})
                        with open('C:/Users/ideapad 320/Desktop/IG機器人/train/{}.jpg'.format(count),'wb') as f:
                            for chunk in r.iter_content(chunk_size=128):
                                f.write(chunk)
                            print('saved:{}.jpg'.format(post['location']))
                    except KeyError:
                        post.update({'fans_number':number_fans[i],'comment_number':0,'location':'train/{}.jpg'.format(count)})
                        with open('C:/Users/ideapad 320/Desktop/IG機器人/train/{}.jpg'.format(count),'wb') as f:
                            for chunk in r.iter_content(chunk_size=128):
                                f.write(chunk)
                            print('saved:{}.jpg'.format(post['location']))
                if (count%size)>=170:
                    try:
                        post.update({'fans_number':number_fans[i],'comment_number':len(data_load[count]['comments']),'location':'test/{}.jpg'.format(count)})
                        with open('C:/Users/ideapad 320/Desktop/IG機器人/test/{}.jpg'.format(count),'wb') as f:
                            for chunk in r.iter_content(chunk_size=128):
                                f.write(chunk)
                            print('saved:{}.jpg'.format(post['location']))
                    except KeyError:
                        post.update({'fans_number':number_fans[i],'comment_number':0,'location':'test/{}.jpg'.format(count)})
                        with open('C:/Users/ideapad 320/Desktop/IG機器人/test/{}.jpg'.format(count),'wb') as f:
                            for chunk in r.iter_content(chunk_size=128):
                                f.write(chunk)
                            print('saved:{}.jpg'.format(post['location']))
            count+=1
        data_tmp=json.dumps(data_load)
    #with open('test.json','w',encoding="utf-8") as data:

    with open('C:/Users/ideapad 320/Desktop/IG機器人/{}.json'.format(i),'w',encoding="utf-8") as data:
        data.write(data_tmp)