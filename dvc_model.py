# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:38:50 2018

@author: jcao2014
"""

from pandas import read_table
from re import match, search
from random import choice
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep

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

def getHref(data):
    result = ('','')
    try:
        baseUrl = 'http://www.baidu.com/s'
        page = 1
        data = {'wd': data,
                'pn': str(page - 1) + '0',
                'tn': 'baidurt',
                'ie': 'utf-8',
                'bsst': '1'}
        data = baseUrl + '?' + urlencode(data)
        data = Request(data, headers=genHeader())
        data = urlopen(data).read()
        for i in BeautifulSoup(data).find_all(class_='f'):
            href = str(i.find('a').attrs['href'])
            if match(r'^http\:\/\/detail\.zol\.com\.cn\/cell_phone\/index([0-9]*)\.shtml$',href): 
                result = (href,'手机')
                break
            elif match(r'^http\:\/\/detail\.zol\.com\.cn\/tablepc\/index([0-9]*)\.shtml$',href):
                result = (href,'平板')
                break
            elif match(r'^http\:\/\/detail\.zol\.com\.cn\/hd-player\/index([0-9]*)\.shtml$',href):
                result = (href,'电视播放器')
                break
            elif match(r'^http\:\/\/detail\.zol\.com\.cn\/gpsdvd\/index([0-9]*)\.shtml$',href):
                result = (href,'车载播放器')
            else:
                continue
    except Exception as e:
        with open('baidu_err','a') as f:
            print(data, str(e),file=f)
    finally:
        return result


def getName(data):
    result = ('','','')
    try:
        data = Request(data, headers=genHeader())
        data = urlopen(data).read()
        data = BeautifulSoup(data)
        brand = ''
        name = ''
        alias = ''
        if data.find(class_='breadcrumb__manu'):
            brand_obj = data.find(class_='breadcrumb__manu')
            brand = brand_obj.get_text()
            brand = brand.strip().strip('手机').strip('平板电脑').strip()
        if data.find(class_='product-model__name'):
            name_obj = data.find(class_='product-model__name')
            name = name_obj.get_text()
            name = name.strip().strip(brand).strip()
        if data.find(class_='product-model__alias'):
            alias_obj = data.find(class_='product-model__alias')
            alias = alias_obj.get_text()
            alias = alias.strip().strip('别名：').strip()
        result = (brand, name, alias)
    except Exception as e:
        with open('zol_err','a') as f:
            print(data, str(e),file=f)
    finally:
        return result

df0 = read_table('mdm0815', names=['manufact', 'dvc_model', 'cont', 'data'], dtype='str')
del df0['data']
df0.fillna('0', inplace=True)
df0['cont'] = df0['cont'].apply(lambda x: int(x.strip()) if match(r'^[0-9]*$', x.strip()) else 0)
df0 = df0[df0['cont']>99]
df0 = df0.reset_index(drop=True)
df0.fillna('', inplace=True)
cleaner = lambda x: '' if search(r'unknown|UNKNOWN|empty|EMPTY', str(x)) else str(x)
df0['manufact'], df0['dvc_model'] = df0['manufact'].apply(cleaner), df0['dvc_model'].apply(cleaner)

with open ('dvc_model_0816.txt', 'a') as f:
    print('\t'.join(('manufact','model','count','category','brand','name','alias','href')), file=f)
    for index, row in df0.iterrows():
        try:
            manufact = row[0].strip()
            model = row[1].strip()
            ct = str(row[2])
            print(index,manufact,model)
            search_key = manufact + ' ' + model + " site:detail.zol.com.cn"
            href, ctgr= getHref(search_key)
            brand, name, alias = getName(href)            
            result =(x.replace('\t','') for x in (manufact,model,ct,ctgr,brand,name,alias,href))
            print('\t'.join(result), file = f)
            sleep(3)
        except: continue
