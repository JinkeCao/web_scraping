# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:33:01 2021

@author: jkcao
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from func_timeout import func_set_timeout, FunctionTimedOut
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from random import choice
import os
# DevTools listening on ws://127.0.0.1:52024/devtools/browser/5bd6e261-2d1f-41c4-96b8-4a03f5849fa7
# [32140:34904:1117/030710.182:ERROR:chrome_browser_main_extra_parts_metrics.cc(226)] crbug.com/1216328: Checking Bluetooth availability started. Please report if there is no report that this ends.
# [32140:34904:1117/030710.182:ERROR:chrome_browser_main_extra_parts_metrics.cc(229)] crbug.com/1216328: Checking Bluetooth availability ended.
# [32140:34904:1117/030710.182:ERROR:chrome_browser_main_extra_parts_metrics.cc(232)] crbug.com/1216328: Checking default browser status started. Please report if there is no report that this ends.
# [32140:34904:1117/030710.182:ERROR:chrome_browser_main_extra_parts_metrics.cc(236)] crbug.com/1216328: Checking default browser status ended.
# [32140:10108:1117/030710.203:ERROR:device_event_log_impl.cc(214)] [03:07:10.205] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 连到系统上的设备没有发挥作用。 (0x1F)
# CreateFile() Error: 5
# [32140:10108:1117/030710.278:ERROR:device_event_log_impl.cc(214)] [03:07:10.278] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 连到系统上的设备没有发挥作用。 (0x1F)
# CreateFile() Error: 5

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
def link2mht(link):
    
    driver = webdriver.Chrome(r'C:\Users\jkcao\Documents\Python Scripts\chromedriver.exe')
    driver.implicitly_wait(9)
    try:
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
        driver.quit()
        return res['data']
    except Exception as e:
        driver.quit()
        return str(e)

def timered_link2mht(link):
    try:
        mht = link2mht(link)
    except FunctionTimedOut:
        mht = 'TimedOut'
    except Exception as e:
        mht = str(e)
    return mht

@func_set_timeout(99)
def link2bso(link):
    driver = webdriver.Chrome (r'C:\Users\jkcao\Documents\Python Scripts\chromedriver.exe')
    driver.implicitly_wait(9)
    try:
        driver.get(link)
        sleep(1)
        
        while True:
            height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            sleep(1)
            next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            if height == next_height:
                break
        
        bso = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return bso
    except Exception as e:
        driver.quit()
        return str(e)
        

def timered_link2bso(link):
    try:
        bso = link2bso(link)
    except FunctionTimedOut:
        bso = 'TimedOut'
    except Exception as e:
        bso = str(e)
    return bso

# #google
# urls = ('janes.com'
#         ,'defense.gov'
#         ,'space.com'
#         ,'raytheon.com'
#         ,'lockheedmartin.com'
#         ,'defensenews.com'
#         ,'iai.co.il'
#         ,'idexuae.ae'
#         ,'thalesgroup.com'
#         ,'rusi.org'
#         ,'nato.int')
# kw = 'f 16'
# main_url = r'https://www.google.com/search?'

# for url in urls:
#     path = r'D:/mb/' + url.split('.')[0] + r'/'
#     if not os.path.exists(path): os.makedirs(path)
#     data = {'q':'site:' + url + ' ' + kw, 'tbm':'nws'}
#     link = main_url + urlencode(data)
    
#     try:
#         bso = timered_link2bso(link)
#         for g_card in bso.find_all('g-card'):
#             try:
#                 with open(path + g_card.find(role='heading').get_text().strip() +'.mht', 'w', newline='', encoding='utf8') as fout:
#                     fout.write(timered_link2mht(g_card.find('a')['href']))
#             except: continue
#     except: continue

#baidu+google
sites =['dsti.net'
        ,'scspi.org'
        ,'sicc.org.cn'
        ,'knowfar.org.cn'
        ,'military.china.com']
kws = {'target': ['幻影2000战斗机','F-16A/B战斗机','F-16V战斗机','F/A-18E/F战斗机','IDF战斗机','RC-135电子侦察机','P-1反潜巡逻机','P-3C反潜巡逻机','E-2K预警机','EP-3电子侦察机','EP-电子侦察机','OP-3照相侦察机','阿武隈级大淀号护卫舰','阿武隈级利根号护卫舰','阿武隈级筑摩号护卫舰','伯克级麦凯恩号驱逐舰','朝雾级朝雾号驱逐舰','朝雾级山雾号驱逐舰','朝雾级泽雾号驱逐舰','成功级班超号护卫舰','成功级成功号护卫舰','成功级逢甲号护卫舰','成功级继光号护卫舰','成功级铭传号护卫舰','成功级岳飞号护卫舰','成功级张骞号护卫舰','成功级郑和号护卫舰','冲绳嘉手纳空军基地','村雨级春雨号驱逐舰','村雨级村雨号驱逐舰','村雨级雷号驱逐舰','村雨级夕立号护卫舰','基隆级基隆号驱逐舰','基隆级马公号驱逐舰','基隆级苏澳号驱逐舰','基隆级左营号驱逐舰','济阳级凤阳号护卫舰','济阳级淮阳号护卫舰','济阳级宁阳号护卫舰','济阳级宜阳号护卫舰','康定级承德号护卫舰','康定级康定号护卫舰','康定级康定号护卫舰','尼米兹级罗斯福号航母','秋月级秋月号驱逐舰','十和田级滨名号补给舰','“滨名”号油弹补给舰','伯克级麦凯恩号驱逐舰','台南台','星星广播电台','苏澳基地','台北基地','岩国基地','长滨基地','左营基地','屏东基地','青森基地','鹿屋基地','那霸基地','淡水基地','花莲基地','基隆基地','把霸基地']
       ,'communication':['Link-11高频数据链通信系统','日自卫队航空兵通信网','RT-7000”高频数据传真系统','“安讯7号”短波电报译电自动化系统','基隆渔船网','星星广播电台','国际民航通信网']
       ,'radar': ['AN/FPS-117','CS/UPS-200C','CS/FPS-500S','AN/APS-145','RDY','AN/APG-66','AN/APG-83','GD-53','J/FPS-4','AN/APS-137','OPS-24','OPS-14','OPS-28','AN/APG-79','AN/SPY-1A','AN/SPS-48E']}

for x1 in kws:
    for x2 in kws[x1]:
        for x3 in sites:
            data = {'q':'site:' + x3 + ' ' + x2}
            link = r'https://www.google.com/search?' + urlencode(data)
            try:
                bso = timered_link2bso(link)
                # print(len(bso.find_all('div', class_='g')))
                for g in bso.find_all('div', class_='g'):
                    h3 = x2
                    for c in r'<>/\|:*? ': h3 = h3.replace(c, '_')
                    h4 = g.find('h3').get_text().strip()
                    for c in r'<>/\|:*? ': h4 = h4.replace(c, '_')
                    path = r'D:/mb/' + x3.split('.')[0] + r'/' + x1 + r'/' + h3 + r'/'
                    if not os.path.exists(path): os.makedirs(path)
                    print(h4)
                    with open(path + h4 +'.mht', 'w', newline='', encoding='utf8') as fout:
                        fout.write(timered_link2mht(g.find('a')['href']))
            except Exception as e:
                print(str(e))
                continue
                
            
            
        
        

