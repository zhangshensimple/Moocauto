from business.login_business import LoginBusiness
from selenium import webdriver
import unittest,os,time,ddt
import HTMLTestRunner
from utools.excel_reddutool import ExcelUtools



class LoginCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get('https://www.imooc.com/user/newlogin')
		self.driver.maximize_window()
		self.login = LoginBusiness(self.driver)

	def tearDown(self):
		time.sleep(2)
		for method_name,error in self._outcome.errors:
			if error:
				case_name = self._testMethodName
				file_name = os.path.join(os.getcwd()+'/image/'+case_name+'.png')
				self.driver.save_screenshot(file_name)
		self.driver.close()

	def test_login_name_error(self):
		name_error = self.login.login_name_error('asdaf','1234354')
		return self.assertTrue(name_error,'测试失败')

	def test_login_password_error(self):
		password_error = self.login.login_password_error('15562576593','1234')
		return self.assertTrue(password_error)




if __name__ =='__main__':
	file_path = r'D:\PycharmProjects\Moocauto\report\login_case_report.html'
	f = open(file_path,'wb')
	suite = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
	runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='ddt_report01',description='SECOND')
	runner.run(suite)