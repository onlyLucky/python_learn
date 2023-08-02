'''
Author: fg
Date: 2023-08-02 19:39:04
LastEditors: fg
LastEditTime: 2023-08-02 21:58:40
Description: 计算三角形的面积
'''
import cmath

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a+b+c)/2

# 计算面积
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('三角形面积为 %0.2f' %area)
area = cmath.sqrt((s*(s-a)*(s-b)*(s-c)))
print('三角形面积为{0:0.2f}'.format(area.real))