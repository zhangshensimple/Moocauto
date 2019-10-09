#coding=utf-8
import xlrd

class ExcelUtools(object):
	def __init__(self,excel_filepath=None,index=None):
		if excel_filepath == None:
			excel_filepath = r'D:\PycharmProjects\Moocauto\config\login_case_data.xls'
		if index == None:
			index = 0
			self.data = xlrd.open_workbook(excel_filepath)
			self.table = self.data.sheets()[index]
			#行数
			self.rows = self.table.nrows

	def get_data(self):
		result = []
		for i in range(self.rows):
			column = self.table.row_values(i)
			result.append(column)
		return result

if __name__ =='__main__':
	ex =ExcelUtools()
	ex.get_data()
