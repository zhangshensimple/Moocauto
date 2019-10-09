#coding=utf-8

from utools.read_localElement_ini import ReadIni
from selenium import webdriver

class FindElement(object):
	def __init__(self,driver):
		self.driver = driver
	#根据元素名获取元素的定位方式和值
	def get_element(self,key):
		read_ini = ReadIni()
		data = read_ini.get_value(key)
		by = data.split(':')[0]
		value =  data.split(':')[1]
		try:
			if by == 'id':
				return self.driver.find_element_by_id(value)
			elif by == 'classname':
				return self.driver.find_element_by_classname(value)
			elif by == 'xpath':
				return self.driver.find_element_by_xpath(value)
			else:
				return self.driver.find_element_by_css(value)
		except:
			return None

