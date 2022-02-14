# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from os import system, listdir
# from __future__ import unicode_literals
# import youtube_dl
from func_timeout import func_set_timeout, FunctionTimedOut
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
# import bilili
# b = bilili()

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

@func_set_timeout(999)
def gbili(url):
    # system(
    #     r'bilili --danmaku no -d C:\Users\jkcao\Videos\tmp' 
    #     + r' --playlist-type no -y ' 
    #     + r'https:'
    #     + url
    #     )
    system(
        r'you-get --no-caption -o C:\Users\jkcao\Videos\tmp\ '
        + url
        )

def timered_gbili(url):
    try: gbili(url)
    except FunctionTimedOut: print('gibili timeout')
    except Exception as e: print(str(e))

@func_set_timeout(999)    
def ubili(tmp, rp):
    with SSHClient() as ssh:
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(
            hostname=''
            , port=0
            , username=''
            , password=''
            )
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(
                tmp
                ,recursive=True
                ,remote_path=rp
                )
def timered_ubili(tmp, rp):
    try: ubili(tmp, rp)
    except FunctionTimedOut: print('ubili timeout')
    except Exception as e: print(str(e))

# system(r"bilili --danmaku 'no' https://www.bilibili.com/video/BV1444y1H7hy")
# bilili --danmaku no -d D:\20220208_dy\ --playlist-type no -y https://www.bilibili.com/video/BV1bE411T7yk
# 【教程】平面设计零基础入门到品牌进阶全套系统课程 软件基础篇（PS+AI+精修+合成） - bilibili

for k in (
        'AI合成'
        ,'合成语音'
        ,'伪造语音'
        ,'合成音频'
        ,'伪造音频'
        ,'deepfake'
        ,'deepfake-voice'
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
                        if r'http:' not in li.a['href'].split('?')[0]:
                            url = r'http:' + li.a['href'].split('?')[0]
                        else:
                            url = li.a['href'].split('?')[0]
                        try:
                            timered_gbili(url)
                            sleep(9)
                        except: pass
                        s = 0
                        while r'.download' in ' '.join(listdir(r'C:\Users\jkcao\Videos\tmp')) or len(listdir(r'C:\Users\jkcao\Videos\tmp')) != 1:
                            sleep(9)
                            s += 1
                            if s > 111: break
                        
                        ld = listdir(r'C:\Users\jkcao\Videos\tmp')
                        try:
                            timered_ubili(
                            tmp='C:\\Users\\jkcao\\Videos\\tmp\\' + ld[0]
                            , rp = '/iflytek/jkcao/bili/' + k
                            )
                            sleep(9)
                        except: pass
                        while len(listdir(r'C:\Users\jkcao\Videos\tmp')) > 0:
                            for d in ld:
                                system(
                                    r'del /f /s /q "'
                                    + 'C:\\Users\\jkcao\\Videos\\tmp\\'
                                    + d
                                    + '"'
                                    )
                                sleep(1)
                    except: continue
            else: break
        except Exception as e:
            print(str(e))
            continue
