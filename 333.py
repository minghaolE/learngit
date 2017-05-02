# coding:utf-8
#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import os
import random
import sys
import os.path
import urllib
import urllib2
'''
kw = raw_input('pls input a kw:')
print(kw)
'''
pn = raw_input('pls input a page number:')
url = 'http://1024.luj8le.click/pw/thread.php?fid=16&page=' + pn
url1 = 'http://1024.luj8le.click/pw/'


UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def get_request_headers():
    request_headers = {
        'User-Agent': random.choice(UserAgent_List),  
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        }
    return request_headers

def get_torrent_headers():
    torrent_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www2.j32048downhostup9s.info',
        'Origin': 'http://www2.j32048downhostup9s.info',
        'Referer': 'http://www2.j32048downhostup9s.info',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(UserAgent_List),
    }
    return torrent_headers
def get_url(url):
    get = requests.get(url)
    print(get)
#   print(get.text)
    return get_url


#get_url(url)
#get photo list
def links_1024(get_url):
    get_url = requests.get(url,headers = get_request_headers())
    soup = BeautifulSoup(get_url.text,'lxml')
    links = soup.select('tr.tr3 > td > h3 > a')
    links_1024 = []
    for link in links:
        if 'htm_data' in link.get('href'):
            url2 = url1 + link.get('href')  
            links_1024.append(url2)
        else:
        	pass
    print links_1024
    return links_1024


def ope1(links_1024):
	for l in links_1024:
#		print l 
		i = requests.get(l)
		soup = BeautifulSoup(i.text,'lxml')
		links = soup.select('tr > th > div > img or a')
		links_list = []
		for  link in links:
			if 'http' in link.get('src or href'):
				picimg = link.get('src or href')
				links_list.append(picimg)
			else:
				pass
		print(l)
		print(links_list)
	return ope1


'''
def get_name():
    for l in links_1024:
#       print l 
        i = requests.get(l)
        soup = BeautifulSoup(i.text,'lxml')
        links = soup.select('tr > th > div > img')
    name = 

def dow_pic(ope1):
    urllib.urlretrieve(ope1 % (get_name))
    return dow_pic 
'''

    

get_url(url)
links_1024(get_url)
ope1(links_1024(get_url))
#dow_pic(ope1)
#ope2(ope1)
#get_links_1024(links_1024)

