'''
Author: fg
Date: 2023-08-03 09:18:13
LastEditors: fg
LastEditTime: 2023-08-03 09:21:27
Description: 圆形面积
'''
def circular_area(r):
    PI = 3.142
    return PI*(r*r)

print('圆的面积为 %.6f' %circular_area(5))