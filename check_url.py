# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup  
import requests  
import csv  
import bs4  

# 检查是否可以链接网页
def check_link(url):  
    try:  
        r = requests.get(url)  
        r.raise_for_status()  
        r.encoding = r.apparent_encoding  
        return r.text  
    except:  
        print('无法链接服务器！！！')

#爬取资源  
def get_contents(ulist,rurl):  
    soup = BeautifulSoup(rurl,'lxml')  
    trs = soup.find_all('tr')  
    for tr in trs:  
        ui = []  
        for td in tr:  
            ui.append(td.string)  
        ulist.append(ui)  
        
