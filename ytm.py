# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:50:52 2019

@author: jcao2014
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="C:\\Users\\jcao2014\\3D Objects\\geckodriver.exe")
driver.get("https://danjuanapp.com/djmodule/value-center")
sleep(3)

js = "var q=document.body.scrollTop=100000"
driver.execute_script(js)
sleep(3)

bsObj = BeautifulSoup(driver.page_source)

keys = []
for i in bsObj.find("div",class_="out-row").find_all("a"):
    try:
        this_key = i.find("small").get_text() + "_" + i.find("h1").get_text()
        this_key = this_key.strip()
        keys.append(this_key)
    except:
        continue

values = []
for i in bsObj.find("div",class_="in-row").find_all("a"):
    try:
        pe = i.find(class_='pe').get_text()
        pe = float(pe.strip().strip("'"))
        pb = i.find(class_='pb').get_text()
        pb = float(pb.strip().strip("'"))
        dyr = i.find(class_='dyr').get_text()
        dyr = float(dyr.strip().strip("'").strip("%"))/100
        this_value = [pe,pb,dyr]
        values.append(this_value)
    except:
        continue
driver.close()

x = dict(zip(keys, values))
y = {}
for i in x:
    ytm = x[i][1] / x[i][0] + x[i][2] * (1 - x[i][1])
    y[i] = ytm

y = sorted(y.items(), key=lambda d: d[1], reverse=True)
for i in y:
    print(i[0], i[1], x[i[0]], sep='\t')
