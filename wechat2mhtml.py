# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:49:05 2021

@author: jkcao
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from func_timeout import func_set_timeout, FunctionTimedOut

@func_set_timeout(99)
def link2mht(link, title, head, time):
    
    driver = webdriver.Chrome(r'C:\Users\jkcao\Documents\Python Scripts\chromedriver.exe')
    driver.implicitly_wait(9)
    driver.get(link)
    sleep(1)
    
    while True:
        height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(1)
        next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
        if height == next_height:
            break
        
    res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
    try:
        dt = driver.find_element_by_id('publish_time').text.strip()
    except:
        dt = time
    with open(r'D:/dingba_wechat/'+dt+'_'+title+'_'+head+'.mht', 'w', newline='', encoding='utf8') as fout:
        fout.write(res['data'])
    driver.quit()

with open('dingba_wechat.tsv', encoding='utf8') as fin:
    for i in fin:
        
        info = i.split('\t')
        if '】' in info[1] and '【' in info[1]:
            head = info[1].split('】')[-1]
            title = info[1].split('【')[-1].split('】')[0]
        else:
            head = info[1]
            title = ''
        for i in r'<>/\|:*? ':
            head = head.replace(i, '+')
        link = info[-1].split('#')[0]
        try:
            link2mht(link, title, head, info[0])
        except FunctionTimedOut:
            with open(r'D:/dingba_wechat/failure_log.tsv', 'a', encoding='utf8') as fl:
                print('website cannot be loaded in 99 seconds', title, head, link, sep='\t', file=fl)
            continue
        except Exception as e:
            with open(r'D:/dingba_wechat/failure_log.tsv', 'a', encoding='utf8') as fl:
                print(str(e), title, head, link, sep='\t', file=fl)
            continue
# link2mht(r'http://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651119717&idx=1&sn=b0d4ff99724ebd38c7b500d1ff564303&chksm=f1ae975fc6d91e494a59a28c91089da3dec735b82cfe7eafb6b11bec8b5a6ae682ccfe5fe6f5&scene=21#wechat_redirect', 'title', 'head')
