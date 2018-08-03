# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 09:55:54 2018

@author: jcao2014
"""
from random import choice
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from time import sleep
from json import loads, dumps

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

def flatten_detail(d):
    d = [d['description'],#2
         d['fileSize'],#3
         d['appName'],#4
         d['categoryName'],#5
         d['apkMd5'],#6
         d['appDownCount'],#7
         d['authorName'],#8
         d['newFeature'],#9
         d['pkgName'],#10
         d['versionCode'],#11
         d['versionName'],#12
         d['averageRating'],#13
         d['editorIntro'],#14
         d['apkPublishTime'],#15
         d['appRatingInfo']['ratingCount'],#16
         d['appRatingInfo']['ratingDistribution']['1'],
         d['appRatingInfo']['ratingDistribution']['2'],
         d['appRatingInfo']['ratingDistribution']['3'],
         d['appRatingInfo']['ratingDistribution']['4'],
         d['appRatingInfo']['ratingDistribution']['5']]
    d = [dumps(x, ensure_ascii=False) for x in d]
    d = [x.replace('\t',' ') for x in d]
    d = '\t'.join(d)
    return d

baseUrl = 'http://sj.qq.com/myapp/searchAjax.htm?'
# filein = 'apps.txt'
qqout = 'apps_qq_v0.txt'
cleanout = 'apps_clean_v0.txt'
app = {}
app_nf = []
kw = ('信用卡','代还信用卡','信用卡代还')

for i in kws:
    try:
        with open(i+'_360.txt') as f:
            with open(qqout, 'a') as g:
                for j in f:
                    j = j.strip()
                    if j in app:
                        print(j)
                        print(i + '\t' + j +'\t' + app[j], file=g)
                    elif j in app_nf:
                        continue
                    else:
                        try:
                            data = {'kw': j}
                            data = baseUrl + urlencode(data)
                            data = Request(url=data, headers=genHeader())
                            data = urlopen(data).read()
                            sleep(3)
                            data = data.decode()
                            data = loads(data)
                            for k in data['obj']['items']:
                                if j in k['appDetail']['appName'] or k['appDetail']['appName'] in j:
                                    print(j, k['appDetail']['appName'])
                                    fd = flatten_detail(k['appDetail'])
                                    print(i + '\t' + j +'\t' + fd, file=g)
                                    app[j] = fd
                        except Exception as e:
                            with open('err.txt', 'a') as f:
                                print(j + '\t' + str(e), file = f)
                            app_nf.append(j)
                            continue
    except Exception as e:
        print('outer', str(e))
        continue
# for i in kw:
#     with open(i+'_360.txt') as f:
#         with open(qqout, 'a') as g:
#             for j in f:
#                 j = j.strip()
#                 try:
#                     data = {'kw': j}
#                     data = baseUrl + urlencode(data)
#                     data = Request(url=data, headers=genHeader())
#                     data = urlopen(data).read()
#                     sleep(3)
#                     data = data.decode()
#                     data = loads(data)
#                     for k in data['obj']['items']:
#                         if j in k['appDetail']['appName'] or k['appDetail']['appName'] in j:
#                             print(j, k['appDetail']['appName'])
#                             fd = flatten_detail(k['appDetail'])
#                             print(i + '\t' +  j +'\t' + fd, file=g)
#                 except Exception as e:
#                     with open('apps_err.txt', 'a') as f:
#                         print(j + '\t' + str(e), file = f)
#                     continue

# with open(qqout) as f:
#     with open(cleanout,'a') as g:
#         for j in f:
#             j = j.split('\t')
#             k = j[13]+ j[1]+j[3]
#             mark = False
#             for l in ('保险','车险','汽车险','汽车保险','车保险','旅行险','旅行保险','旅游险','旅游保险','意外保险','意外险','财产保险','财产险','财险','财保','保险咨询','健康保险','健康险','人寿险','人寿保险','寿险','人保','保单'):
#                 if l in k:
#                     mark = True
#             for m in ('综合金融','金融生活服务','金融服务','保险箱','保险柜','保险师','保险代理人','展业','代理人','计划书','保险从业人员','保险从业','保险销售','卖保险'):
#                 if m in k:
#                     mark = False                            
#             if mark == True: print('\t'.join(j).strip(), file = g)
kws = ('信用卡','账单日','还款','还卡','额度', '调额')
with open(qqout) as f:
    with open(cleanout,'a') as g:
        print('关键词' + '\t' + '原始名称' + '\t' + '描述' + '\t' + '文件大小' + '\t' + 'app名称' + '\t' + '类别名称' + '\t' + '安装包md5' + '\t' + 'app下载量' + '\t' + '开发者名称' + '\t' + '新特性' + '\t' + '安装包名称' + '\t' + '版本号' + '\t' + '版本名称' + '\t' + '平均打分' + '\t' + '编辑推荐语' + '\t' + '安装包发布时间' + '\t' + '总打分人数' + '\t' + '1分人数' + '\t' + '2分人数' + '\t' + '3分人数' + '\t' + '4分人数' + '\t' + '5分人数' + '\t' + '\t'.join(kws), file = g)
        for j in f:
            j = j.strip()
            s = j.split('\t')
            k = s[14]+ s[2]+s[4]
            mark = 0
            for l in kws:
                c = 0
#                 if l == '车险':
#                     c = k.count(l) - k.count('汽车险')
#                 elif l == '寿险':
#                     c = k.count(l) - k.count('人寿险')
#                 elif l == '车保险':
#                     c = k.count(l) - k.count('汽车保险')
#                 else:
                c = k.count(l)
                j += '\t'
                j += str(c)
                mark += c
            
#             if mark < 4:
#                 mark = 0
#             k = k.replace('股票代码', '')
#             for m in ('综合金融','金融生活服务','金融服务','保险箱','保险柜','保险师','保险代理人','展业','代理人','计划书','保险从业人员','保险从业','保险销售','卖保险','借款','借贷','社保','五险一金','养老保险','公积金','管理系统','期货','证券','金融产品','股票','车险代理商','信用卡'):
#                 if m in k:
#                     mark = 0
#             if len(eval(s[7])) < 4:
#                 mark = 0
#             if mark != 0:
#                 print(mark)
            if mark != 0: print(j, file = g)
