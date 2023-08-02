'''
Author: fg
Date: 2023-08-02 19:04:57
LastEditors: fg
LastEditTime: 2023-08-02 19:24:36
Description: 平方根
'''
# 导入复数数学模块
import cmath

num = float(input('请输入一个数字：'))
num_sqrt = num**0.5
num_sqrt1 = cmath.sqrt(num)
print('%0.3f 的平方根为 %0.3f'%(num, num_sqrt))

print('使用复数数学模块计算的{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt1.real,num_sqrt1.imag))