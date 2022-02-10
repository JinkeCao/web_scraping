# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from os import system
# from __future__ import unicode_literals
# import youtube_dl
from func_timeout import func_set_timeout, FunctionTimedOut
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode


@func_set_timeout(99)
def link2bso(link):
    driver = webdriver.Chrome(r'C:\Users\jkcao\Downloads\chromedriver.exe') 
    driver.implicitly_wait(9)
    try:
        driver.get(link)
        sleep(1)
        c = 0
        while True:
            height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            sleep(1)
            next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            c += 1
            if c > 22: break
            elif height == next_height: break
        bso = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return bso
    except Exception as e:
        driver.quit()
        return str(e)
        

def timered_link2bso(link):
    try: bso = link2bso(link)
    except FunctionTimedOut: bso = BeautifulSoup('TimedOut', 'html.parser')
    except Exception as e:
        print(str(e))
        bso = BeautifulSoup(str(e), 'html.parser')
    return bso

# system(r"bilili --danmaku 'no' https://www.bilibili.com/video/BV1444y1H7hy")
# bilili --danmaku no -d D:\20220208_dy\ --playlist-type no -y https://www.bilibili.com/video/BV1bE411T7yk

for k in (
        'AI合成'
        ,'合成语音'
        ,'伪造语音'
        ,'合成音频'
        ,'伪造音频'
        ,'deepfake'
        ,'deepfake voice'
        ,'假音'
        ,'仿声'
        ,'声音模仿'
        ,'深度伪造'
        ,'AI主播'
        ):
    for p in range(1,51):
        print(k, p)
        try:
            l = 'https://search.bilibili.com/all?' + urlencode({'keyword': k,'page': p})
            bso = timered_link2bso(l)
            sleep(9)
            if len(bso.find_all(class_='video-item matrix'))>0:
                for li in bso.find_all(class_='video-item matrix'):
                    try:
                        system(r'bilili --danmaku no -d C:\Users\jkcao\Videos' + r'/' + k + r'/' + r' --playlist-type no -y ' + r'https:'+li.a['href'].split('?')[0])
                        sleep(9)
                    except: continue
            else: break
        except: continue




# # youtube-dl -f 2 https://www.bilibili.com/video/BV1mZ4y1c73Q
# x = {
#       'h': [r'https://www.bilibili.com/video/BV1TR4y1n7YU']
#         }
# for i in x:
#     try:
#         ydl_opts = {#'sleep_interval': 9
#                     # ,'socket_timeout':99
#                     'format':r'2'
#                     ,'outtmpl':r'd:/20220208_dy/' + r'%(title)s.%(ext)s'
#                     # ,'ignoreerrors': True
#                     # ,'continuedl':True
#                     # ,'listformats':True
#                     # ,'forceurl':True
#                     # ,'retries': 5
#                     }
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download(x[i])

            
#     except Exception as e:
#         print(str(e))

