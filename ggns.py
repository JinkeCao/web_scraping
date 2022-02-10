# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:04:07 2022

@author: jkcao
"""

# from random import choice
from urllib.parse import urlencode
# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from func_timeout import func_set_timeout, FunctionTimedOut
# import os
from json import dump
from newspaper import Article
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver import Firefox
import opencc
cc = opencc.OpenCC('t2s')
  

@func_set_timeout(99)
def link2bso(link):
    driver = webdriver.Chrome(r'C:\Users\jkcao\Downloads\chromedriver.exe')
    # options = Options()
    # service = Service(r'C:\Users\jkcao\Downloads\geckodriver.exe')
    # options.set_preference('profile', r"C:\Users\jkcao\AppData\Roaming\Mozilla\Firefox\Profiles\profiles.txt")
    # options.headless = False
    # driver = Firefox(r'C:\Users\jkcao\Downloads\geckodriver.exe', options=options)
    #, firefox_profile=FirefoxProfile(r"C:\Users\jkcao\AppData\Roaming\Mozilla\Firefox\Profiles"))
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
    except FunctionTimedOut: bso = 'TimedOut'
    except Exception as e:
        print(str(e))
        bso = str(e)
    return bso



def path_cleaner(path):
    for c in r'<>/\|:*? ': path = path.replace(c, '_')
    return path

# def is_contain_chinese(check_str):
#     for ch in check_str:
#         if u'u4e00' <= ch <= u'u9fff':
#             return True
#         return False

# https://www.google.com/search?q=f+16+fighting+falcon&tbm=nws&start=10
for q in (
'乔建军'
):
    for st in range(0, 1000, 10):
        print(q, st)
        try:
            dt = {'q': q
                  ,'tbm': 'nws'
                  ,'start': st
                  }
            link = r'https://www.google.com.hk/search?' + urlencode(dt)
            bso = timered_link2bso(link)
            # if r'”相关的新闻。' in bso.get_text() and r'未搜到与“' in bso.get_text():
            # if '下一页' not in bso.get_text(): break
            for b in bso.find_all('a', class_='WlydOe'):
                try:
                    ss = [t for t in b.stripped_strings]
                    article = Article(b['href'])
                    article.download()
                    sleep(9)
                    article.parse()
                    if len(article.text) > 0:
                        with open(r'D:/20220126_gn/' + path_cleaner(q) + r'.json'
                                  ,'a'
                                  ,encoding='utf8'
                                  ) as f:
                            dump({'source': ss[0]
                                 ,'title': cc.convert(ss[1])
                                 ,'abstract': cc.convert(ss[2])
                                 ,'time': str(article.publish_date)
                                 ,'authors': article.authors
                                 ,'text': [cc.convert(t) for t in  article.text.split('\n\n')]}
                                 ,fp = f
                                 ,ensure_ascii=False
                                )
                            print(''
                                  ,file=f)
                except Exception as e:
                    print('innner:', str(e))
                    pass
            if '下一页' not in bso.get_text():
                sleep(9)
                break
        except Exception as e:
            print('outer:', str(e))
            pass

