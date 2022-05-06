# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:04:07 2022

@author: jkcao
"""
# python C:\Users\jkcao\.spyder-py3\ggnstb.py
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
# from newspaper import Article, Config
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver import Firefox
# from goose3 import Goose
from gne import GeneralNewsExtractor

# from goose3.text import StopWordsChinese
import opencc

from random import choice

def genHeader():
    headerset = [
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
         "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/45.0.2454.101 Safari/537.36'},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/52.0.2743.116 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"},
        {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}]
    return choice(headerset)
  

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
            if c > 55: break
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

@func_set_timeout(99)
def link2dic(link):
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
        e = GeneralNewsExtractor()
        res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
        # print(11111111, res)
        # result = e.extract(res)
        result = e.extract(driver.page_source)
        # print(11111, result)
        driver.quit()
        return result
    except:
        driver.quit()
        return {}
        

def timered_link2dic(link):
    try:
        dic = link2dic(link)
    except FunctionTimedOut: dic = {}
    except Exception as e:
        print(str(e))
        dic = {}
    return dic


def path_cleaner(path):
    for c in r'<>/\|:*? ': path = path.replace(c, '_')
    return path

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False

# def is_contain_chinese(check_str):
#     for ch in check_str:
#         if u'u4e00' <= ch <= u'u9fff':
#             return True
#         return False
cc = opencc.OpenCC('t2s')


# https://www.google.com/search?q=f+16+fighting+falcon&tbm=nws&start=10
# https://www.google.com/search?q=site:zh.wikipedia.org+%E7%BD%97%E5%BE%B7%E9%87%8C%E6%88%88+%E6%9D%9C%E7%89%B9%E5%B0%94%E7%89%B9&start=10
    

for q2 in ('抗议事件', '抗议活动', '示威', '游行', '镇压', '暴力事件', '骚乱'):
    for st in range(0, 100, 10):
        for q1 in ('www.dw.com', 'www.people.com.cn', 'www.epochtimes.com'):
            print(q2, st)
            try:
                dt = {'q': 'site:' + q1 + ' ' + q2
                      # ,'tbm': 'nws'
                      ,'start': st
                      }
                link = r'https://www.google.com.hk/search?' + urlencode(dt)
                
                bso = timered_link2bso(link)
                # if r'”相关的新闻。' in bso.get_text() and r'未搜到与“' in bso.get_text():
                # if '下一页' not in bso.get_text(): break
                # for b in bso.find_all('div', class_='yuRUbf'):
                for b in bso.find_all('div', class_='g tF2Cxc'):
                    try:
                        # print(b.find('a')['href'])
                        # title = [x for x in b.stripped_strings]
                        g = b.get_text()
                        title = g.split('http')[0]
                        abstract = g.split('网页快照')[-1]                        
                        bs = timered_link2bso(b.find('a')['href'])
                        content = [cc.convert(x) for x in bs.stripped_strings if len(x) > 4 and is_chinese(x)]

                        # ss1 = bs.find('h1', class_='firstHeading mw-first-heading').get_text()
                        # ss2 = ' '.join([x for x in bs.find('div', class_='mw-body-content mw-content-ltr').stripped_strings])#.get_text()#.replace(u'\xa0','')
                        with open(r'D:/20220505_ggwb/' + q2 + '-' + q1 + r'.json'
                                  ,'a'
                                  ,encoding='utf8'
                                  ) as f:
                            dump({'kw': q2
                                   ,'link': q1
                                   ,'title':cc.convert(title)
                                   ,'abstract': cc.convert(abstract)                       
                                   ,'content': content
                                  }
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
    
