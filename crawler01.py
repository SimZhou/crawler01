# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:00:48 2018

@author: Yihua Zhou
"""

from bs4 import BeautifulSoup  
import requests  
import pandas as pd

# 生成三个空列表
HTime = []
HType = []
HPrice = []

# 定义函数
def get_content(url):  
    try:
        r = requests.get(url)  
        r.raise_for_status()  
        r.encoding = r.apparent_encoding  
        return r.text  
    except:  
        print('无法链接服务器！！！') 

# 页面时间
dateId = 1522972800

for x in range(0,520):
    # 页面网址
    url = "http://publisher.theengineshed.com/freshinfo/embedded_prices.php?s=r&ss=mp&fn=prod&date="+str(dateId)+"&up_ord=&cid=&cat1=249&pid=1178&mid=&vid=a&show="

    # 检查是否可以链接网页，并抓取网页
    r = get_content(url)
    
    # 导进好汤 
    sr = BeautifulSoup(r,'lxml')  

    # 将页面保存到文件
    # fw = open('D:/program/projecta/abcd.html','w')
    # print(sr.prettify(),file=fw)
    # fw.close()
    
    # 判断该页表格行数n，并把每列数据写入变量HType，HPrice
    n = 0
    line = sr.find(string = 'Variety - Source').parent.parent.parent.parent.next_sibling.next_sibling
    while not line.find(value = 'Plot graph from selected'):
        HType.append(line.td.next_sibling.text[1:])
        HPrice.append(line.td.next_sibling.next_sibling.string)
        line = line.next_sibling.next_sibling
        n = n + 1
        
    # 获取当日日期
    date_raw = sr.find(string = 'Price of ').parent.next_sibling.next_sibling.string
    date = date_raw[4:]
        
    # 日期写入HTime
    for i in range(0,n):
        HTime.append(date)

    dateId = dateId - 604800
    
    print (x)

# 写入csv
dataframe = pd.DataFrame({'Date':HTime,'Country and quantity':HType,'Price':HPrice})
dataframe.to_csv("D:\\test3.csv",index=False,sep=',')

















