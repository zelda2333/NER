#!/usr/bin/python3
import re
import random
from random import choice
s = '我来到[@1999年#STW*]的[@上海#NUM*]的[@东华大学#PER*]二[@11年#STW*]'
stw = ['@我#STW*','@来#STW*','@到#STW*','@1w99年#STW*','@1992年#STW*']
num = ['19','2','3','4','5']
per = ['自己','你们','他们','我们','庄家']

#随机返回list里面的一个元素
def random_type(type):
	print(choice(type))
	return choice(type)

#随机返回list里多个元素	
def return_repl(type):
	adda=[]
	some = random.sample(type , 10)
	adda.extend(some)
	print(adda)
	return adda

#查找"@....#STW*"并替换
def find_STW():
	pattern = re.compile(r'[@][^@]*?#STW\*')
	repl = random_type(stw)
	replace = re.sub(pattern,repl,s)
	print(replace)
	return replace

if (__name__ == '__main__'):
	find_STW()