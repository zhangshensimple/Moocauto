#coding=utf-8
#读取配置文件中的信息 来操作配置文件(config下的localeElement.ini)

import configparser
import os

class ReadIni(object):
	def __init__(self,filename=None,node=None):
		if filename == None:
			filename = 'D:\PycharmProjects\Moocauto\config\LocalElement.ini'
		if node == None:
			self.node = 'LogInElement'
		else:
			self.node = node
		self.cf = self.load_ini(filename)

#读取配置文件
	def load_ini(self,filename):#加载文件
		cf = configparser.ConfigParser()
		cf.read(filename,encoding='utf-8')
		return cf
#获取丁文方式的值
	def get_value(self,key):
		data = self.cf.get(self.node,key)
		return data

if __name__ == '__main__':
	read_ini = ReadIni()
	print(read_ini.get_value('name'))