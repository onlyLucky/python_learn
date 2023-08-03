'''
Author: fg
Date: 2023-08-03 10:28:11
LastEditors: fg
LastEditTime: 2023-08-03 10:49:14
Description: if语句
'''

num = float(input("输入一个数字："))
if num>0:
	print('正数')
elif num == 0:
	print('零')
else:
	print('负数')

# 内嵌式
if num>=0:
	if num == 0:						
		print('零')
	else:
		print('正数')
else:
	print('负数')
