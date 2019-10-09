#coding=utf-8
from handle.login_handle import LogInHandle

class LoginBusiness(object):
	def __init__(self,driver):
		self.login_h = LogInHandle(driver)

	#输入登录信息 ,并点击操作
	def user_base(self,name,password):
		self.login_h.send_name(name)
		self.login_h.send_password(password)
		self.login_h.click_submit_button()

	#登录成功
	def login_success(self):
		if self.login_h.get_user_text() == None:
			print('登录成功  success')
			return True
		else:
			return False

	#执行操作,用户名错误
	def login_name_error(self,name,password):
		self.user_base(name,password)
		if self.login_h.get_user_text('login_name_error','请输入正确的邮箱或手机号') == None:
			return True
		else:
			return False

	#执行操作,密码错误
	def login_password_error(self,name,password):
		self.user_base(name,password)
		if self.login_h.get_user_text('login_password_error','请输入6-16位密码,区分大小写,不能用空格') == None:
			return True
		else:
			return False

