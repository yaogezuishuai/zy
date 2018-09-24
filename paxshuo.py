import requests
from bs4 import BeautifulSoup

url = 'https://www.cr173.com/new/'
re = requests.get(url)
re.encoding = 'gb2312'
print(re.encoding)
soup = BeautifulSoup(re.text,'lxml')
li_all = soup.find('ul', class_='current').find_all('li')
with open("E:\zy\新建文本文档.txt", 'wb') as f:
    for li in li_all:
        a = li.find_all('a')
        appname = a[1].get_text()+'\r\n'
        print(appname)
        f.write(appname.encode('utf8'))
# a = soup.findAll('a',{"class":{'title'}})
# with open("E:\zy\新建文本文档.txt", 'wb') as f:
#     for t in a:
#         appname = t.get_text()+'\r\n'
#         print(appname)
#         # f.write(appname)
#         f.write(appname.encode('utf8'))
