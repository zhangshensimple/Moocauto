#coding=utf-8
from base.find_element import FindElement

class LoginPage(object):
	def __init__(self,driver):
		self.fd = FindElement(driver)

	def get_name(self):
		return self.fd.get_element('name')
	def get_password(self):
		return self.fd.get_element('password')
	def get_submit(self):
		return self.fd.get_element('submit')
	def get_login_name_error(self):
		return self.fd.get_element('login_name_error')
	def get_login_password_error(self):
		return self.fd.get_element('login_password_error')
	def get_verify_code_error(self):
		return self.fd.get_element('verify_code_error')