# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:14:48 2021

@author: jkcao
"""

# from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.keys import Keys
# from func_timeout import func_set_timeout, FunctionTimedOut
# from pandas import read_table
# from re import match, search
from random import choice
# from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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

# @func_set_timeout(99)
# def link2mht(link, title, head, time):
    
#     driver = webdriver.Chrome(r'C:\Users\jkcao\Documents\Python Scripts\chromedriver.exe')
#     driver.implicitly_wait(9)
#     driver.get(link)
#     sleep(1)
    
#     while True:
#         height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
#         driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
#         sleep(1)
#         next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
#         if height == next_height:
#             break
        
#     res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
#     try:
#         dt = driver.find_element_by_id('publish_time').text.strip()
#     except:
#         dt = time
#     with open(r'D:/dingba_wechat/'+dt+'_'+title+'_'+head+'.mht', 'w', newline='', encoding='utf8') as fout:
#         fout.write(res['data'])
#     driver.quit()

def link2bso(link):
    req = Request(link, headers=genHeader())
    res = urlopen(req).read()
    return BeautifulSoup(res, features="lxml")



def parseLevel3(link, x1, x2, bso, fout):
    try:
        for x in bso.find(class_='usR1').find_all('ul'):
            name = ''
            addr = ''
            tel = ''
            page = ''
            try: name = x.find(class_='li01').get_text('艹').split('艹')[0].replace('\t', ' ')
            except: pass
            try: addr = x.find(class_='li01').get_text('艹').split('艹')[1].replace('\t', ' ')
            except: pass
            try: tel = x.find(class_='li02').get_text('艹').split('艹')[0].replace('\t', ' ')
            except: pass
            try: page = mainPage + x.find_all('li')[0].a['href'].replace('\t', ' ')
            except: pass
            with open(fout, 'a', encoding='utf8') as f: print(link, x1, x2, name, addr, tel, page, sep = '\t', file = f)
    except Exception as e:
        with open(fout, 'a', encoding='utf8') as f: print(link, x1, x2, '', '', '', str(e), sep='\t', file = f)
                
    

mainPage = "http://www.ypsort.com"
fout = "ypsort_level3_20211020.tsv"


# bso = link2bso(mainPage + "/")
# y1 = {x.a.get_text():mainPage + x.a['href'] for x in bso.find(class_='box').find_all('li')}

# print(y1)
# print()

# for y in y1:
#     for z in link2bso(y1[y]).find(class_="usR").find_all('ul'):
#         with open("ypsort_c2_20211019.tsv","a") as fo:
#             print(y, z.a.get_text(), mainPage+z.a['href'],sep = '\t', file = fo
#     sleep(9)


with open('ypsort_c2_20211019.tsv') as f:
    for i in f:
        try:
            x = i.strip().split('\t')
            bso = link2bso(x[-1])
            num = int(bso.find(class_='hpage').get_text().split(' pages ')[0].strip())
            parseLevel3(x[-1], x[0], x[1], bso, fout)
            sleep(9)
            for j in range(num):
                try:
                    if j > 0:
                        bso = link2bso(x[-1] + str(j) + '/')
                        parseLevel3(x[-1], x[0], x[1], bso, fout)
                except: continue
                sleep(9)
        except: continue
                    
                    


