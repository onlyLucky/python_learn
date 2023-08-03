'''
Author: fg
Date: 2023-08-03 10:50:43
LastEditors: fg
LastEditTime: 2023-08-03 11:05:35
Description: 判断字符串是否为数字
'''
import unicodedata
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False

# 测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.37'))
print(is_number('1e3'))

#测试Unicode
#阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False

print(unicodedata.numeric('四')) #4.0