#coding=utf-8
from page.login_page import LoginPage

class LogInHandle(object):
	def __init__(self,driver):
		self.driver = driver
		self.login_p = LoginPage(self.driver)

	#输入用户名
	def send_name(self,name):
		self.login_p.get_name().send_keys(name)
	#输入密码
	def send_password(self,password):
		self.login_p.get_password().send_keys(password)
	#点击确认
	def click_submit_button(self):
		self.login_p.get_submit().click()

	#获取错误信息的文字
	def get_user_text(self,info,user_info):
		try:
			if info == 'login_name_error':
				text = self.login_p.get_login_name_error().text()
			elif info == 'login_password_error':
				text = self.login_p.get_login_password_error().text()
			else:
				text = self.login_p.get_verify_code_error().text()
		except:
			text = None
		return text






