# coding:utf-8
import urllib
import requests
import json
import re

Header = {
    'authorization':'Client-ID d69927c7ea5c770fa2ce9a2f1e3589bd896454f7068f689d8e41a25b54fa6042',
    'accept-version':'v1',
    'Host':'unsplash.com',
    'x-unsplash-client':'web',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
    'Referer':'https://unsplash.com/',
    'Connection':'keep-alive',
    'Accept':'*/*'
}
cnt = 1
page_num = 8
page_url = 'https://api.unsplash.com/napi/feeds/home'
for i in range(page_num):
    print('page'+str(i)+':')
    req = urllib.request.Request(url=page_url,headers=Header)
    html = urllib.request.urlopen(req)
    res = html.read().decode('utf-8')
    hjson = json.loads(res)
    next_page = hjson[u'next_page']
    print(next_page)
    pattern = re.compile('after=(.*)')
    page_bianhao = re.findall(pattern,next_page)[0]
    print(page_bianhao)
    page_url = 'https://api.unsplash.com/napi/feeds/home?after='+page_bianhao
    print(page_url)
    photos = hjson[u'photos']
    for each in photos:
        bianhao = each['id']
        pic = urllib.request.urlopen('https://unsplash.com/photos/'+bianhao+'/download?force=true').read()
        pic_name = str(cnt)+'.jpg'
        cnt += 1
        print('download '+pic_name+'...')
        file = open( 'C:\D\BeautifulPicture\\'+pic_name, 'wb')
        file.write(pic)
        file.close()