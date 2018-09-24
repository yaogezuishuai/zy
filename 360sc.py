from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
import operator

headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) '
                          'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Connection': 'keep-alive', }
#爬取360应用市场最新软件
#获取url集合
'''
爬360市场最新的数据
'''
def get_url():
    url_list = []
    for i in range(-1,10):
        url = "http://zhushou.360.cn/list/index/cid/1/order/newest/?page=" + str(i)
        url_list.append(url)
    return url_list

def ruanj():
    rj_id = entry1.get()
    ruanjian_dict = {}
    for url_s in get_url():
        re = requests.get(url_s,headers=headers)
        bs=BeautifulSoup(re.text,"html.parser")
        items = bs.find('div',attrs={'class':'icon_box'}).find_all('li')
        for ita in items:
            itas = ita.find('a')
            id = int(itas['sid'])
            if id > int(rj_id):
                key = id
                value = ita.get_text()+'：'+'http://zhushou.360.cn'+itas['href']
                ruanjian_dict.update({key: value})
    dict_new = sorted(ruanjian_dict.items(), key=operator.itemgetter(0), reverse=True)#排序
    return dict_new

def main():
    mylist.delete(0.0, END)
    for item in ruanj():
        mylist.insert('insert', item)
        mylist.insert('insert', '\n')

window = tk.Tk()
window.geometry('700x400')
window.title('360市场')

e = StringVar()
entry1 = tk.Entry(window, textvariable=e, fg='red')
e.set('4000000')

mylist = Text(window, width=300)
button = tk.Button(window, text="搜索", command=main)

"""
滚动条
"""
lab = Scrollbar(window)
mylist['yscrollcommand'] = lab.set
lab['command'] = mylist.yview

button.pack()
entry1.pack()
lab.pack(side=RIGHT, fill=Y)
mylist.pack(side=LEFT)

window.mainloop()
