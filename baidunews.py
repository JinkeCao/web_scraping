# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pandas import read_table
from jieba import cut, add_word
from urllib.request import Request, urlopen
from random import choice
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

def word_count(keyword, filein, fileout):    
    add_word(keyword)
    df = read_table(filein)
    df['新闻']=''
    df['词频']=0
    for i in range(0, len(df)):
        try:
            req = Request(df.iloc[i]['链接'], headers=genHeader())
            page = urlopen(req).read()
            sleep(4)
            bs = BeautifulSoup(page)
            news=bs.get_text()
            df.at[i, '新闻']=news
            print(df.iloc[i]['标题'])        
            words = list(cut(news))
            count = 0
            for j in words: 
                if keyword in j: 
                    count+=1
            df.at[i, '词频']=count
            print('word count: ', count)
        except Exception as e:
            print(str(e))
    df.to_excel(fileout)


word_count('讯飞','news_of_iflytek.txt','iflytek_count.xlsx')
word_count('华为','news_of_huawei.txt', 'huawei_count.xlsx')
