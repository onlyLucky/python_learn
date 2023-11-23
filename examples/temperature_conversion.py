'''
Author: fg
Date: 2023-08-03 09:35:05
LastEditors: fg
LastEditTime: 2023-08-03 10:15:52
Description: 摄氏温度转华氏温度
'''
celsius = float(input('输入摄氏温度'))

fahrenheit = (celsius*1.8)+32
print('%0.1f 设施温度转华氏摄氏度为 %0.1f'%(celsius,fahrenheit))