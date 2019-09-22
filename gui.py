#!/usr/bin/python
# coding=utf-8
"""
Version: 1.3
Author: Wangbeng
"""
import shutil
from tkinter import *
import re
import json
import tkinter.filedialog
print(__doc__)
B = 0
A = 0
L = []
c = []
g = 0
h = 0
# f1 = open('text_1.txt', 'r', encoding='utf-8')
# a = f1.read()
# wordlist = re.split('。|？', a)
# juzi_num = len(wordlist)-1
# p2 = re.compile(r'[[](.*?)[]]', re.S)

window = Tk()
window.geometry('1500x1500')
window.title('实体关系')
juzi_num = StringVar()
juzi_num.set('0')
Label(window, text='已选择实体对预览', foreground='red').place(x=50, y=180)
juzi = StringVar()
juzi.set('我是句子')
Label(window, textvariable=juzi).place(x=50, y=30)
Label(window, textvariable=juzi_num, foreground='red').place(x=500, y=10)
juzi_id = StringVar()
juzi_id.set('当前的句子id为  0',)
Label(window, textvariable=juzi_id, foreground='red').place(x=50, y=10)
text1 = Text(window, width=150, height=2)
text1.place(x=50, y=100)
text2 = Text(window, width=150, height=7)
text2.place(x=50, y=200)
v1 = StringVar()
v1.set('')
v2 = StringVar()
v2.set('关系')
v3 = StringVar()
v3.set('')
v4 = StringVar()
v4.set('跳转句子')
a1 = Entry(window, textvariable=v1)
a1.place(x=50, y=450)
a2 = Entry(window, textvariable=v2)
a2.place(x=150, y=450)
a3 = Entry(window, textvariable=v3)
a3.place(x=250, y=450)
a4 = Entry(window, textvariable=v4)
a4.place(x=500, y=450)


def login():
    global L
    L.append({"entity1": v1.get(), "entity2": v3.get(), "relation": v2.get()})
    text2.insert('end', '已选择实体对  %s:%s:%s\n' % (v1.get(), v2.get(), v3.get()))

    # with open('text_1.json', 'a+', encoding='utf-8') as f2:
    #     data = {
    #         'txt_name': r_path,
    #         'txt_re': [
    #             {'sentence_id': A,
    #              'sentence': str(wordlist[A-1]),
    #              'entity and relation': L
    #             }
    #         ]
    #     }
    #     json.dump(data, f2, ensure_ascii=False)
    #     f2.write('\n')
    # print(data)
    v2.set('关系')


def next_zu():
    global h
    h = 0
    global g
    g = 0
    global A
    global c
    text1.delete(0.0, END)
    juzi.set(wordlist[A])
    c = re.findall(p2, wordlist[A])
    for i in c:
        text1.insert('end', i+'   ')
    A = A+1
    juzi_id.set('当前句子的ID为 %d' % A)


def go_to():
    global h
    h = 0
    global g
    g = 0
    global A
    global c
    A = int(a4.get())
    text1.delete(0.0, END)
    juzi.set(wordlist[A-1])
    c = re.findall(p2, wordlist[A-1])
    for i in c:
        text1.insert('end', i + '   ')
    juzi_id.set('当前句子的ID为 %d' % A)


def up_zu():
    global h
    h = 0
    global g
    g = 0
    text1.delete(0.0, END)
    global A
    global c
    A = A-2
    juzi.set(wordlist[A])
    c = re.findall(p2, wordlist[A])
    for i in c:
        text1.insert('end', i + '   ')
    A = A + 1
    juzi_id.set('当前句子的ID为 %d' % A)


def login_true():
    global h
    h = 0
    global g
    global L
    g = 0
    text2.delete(0.0, END)
    with open('text_1.json', 'a+', encoding='utf-8') as f2:
        data = {
            'txt_name': filename1,
            'txt_re': [
                {'sentence_id': A,
                 'sentence': str(wordlist[A - 1]),
                 'entity and relation': L
                 }
            ]
        }
        json.dump(data, f2, ensure_ascii=False)
        f2.write('\n')
    L = []


def save_file():
    shutil.move('text_1.json', 'C:\\Users\\Administrator\\Desktop')


def open_file():
    global filename1
    global a
    global p2
    global wordlist
    filename = tkinter.filedialog.askopenfilename(filetypes=[('All Files', '*')])
    filename1 = filename.split('/')[-1]
    f1 = open(filename, 'r', encoding='utf-8')
    a = f1.read()
    wordlist = re.split('。|？', a)
    juzi_num.set(len(wordlist) - 1)
    p2 = re.compile(r'[[](.*?)[]]', re.S)


def jiaji():
    v2.set('加计')

def buji():
    v2.set('不计')

def jinbaohan():
    v2.set('仅包含')

def kebaohan():
    v2.set('可包含')

def bibaohan():
    v2.set('必包含')

def bubaohan():
    v2.set('不包含')

def fenzhi():
    v2.set('分值')

def zhuangtai():
    v2.set('状态')

def huase():
    v2.set('花色')

def shuliang():
    v2.set('数量')


def caozuo():
    v2.set('操作')


def kaishi1():
    global c
    global g
    global h
    s = len(c)
    v1.set('%s' % (c[g % s]))
    g += 1

def kaishi2():
    global c
    global h
    s = len(c)
    v3.set('%s' % (c[(h + 1) % s]))
    h += 1




b1 = Button(text='选择', command=login)
b1.place(x=50, y=500)
b2 = Button(text='下一组', command=next_zu, bg='red')
b2.place(x=300, y=500)
b3 = Button(text='确定', command=go_to)
b3.place(x=500, y=500)
b4 = Button(text='上一组', command=up_zu)
b4.place(x=350, y=500)
b5 = Button(text='录入', command=login_true)
b5.place(x=100, y=500)
b6 = Button(text='保存文件', command=save_file)
b6.place(x=700, y=500)
b7 = Button(text='  加计  ', command=jiaji)
b7.place(x=50, y=600)
b7 = Button(text='  不计  ', command=buji)
b7.place(x=150, y=600)
b7 = Button(text='  仅包含  ', command=jinbaohan)
b7.place(x=50, y=650)
b7 = Button(text='  可包含  ', command=kebaohan)
b7.place(x=150, y=650)
b7 = Button(text='  必包含  ', command=bibaohan)
b7.place(x=250, y=650)
b7 = Button(text='  不包含  ', command=bubaohan)
b7.place(x=350, y=650)
b7 = Button(text='  分值  ', command=fenzhi)
b7.place(x=50, y=700)
b7 = Button(text='  状态  ', command=zhuangtai)
b7.place(x=150, y=700)
b7 = Button(text='  花色  ', command=huase)
b7.place(x=50, y=750)
b7 = Button(text='  数量  ', command=shuliang)
b7.place(x=150, y=750)
b7 = Button(text='  操作  ', command=caozuo)
b7.place(x=50, y=800)
b7 = Button(text=' 打开文件 ', command=open_file)
b7.place(x=600, y=500)
b7 = Button(text=' 开始1', command=kaishi1)
b7.place(x=150, y=500)
b7 = Button(text=' 开始2', command=kaishi2)
b7.place(x=200, y=500)

mainloop()











