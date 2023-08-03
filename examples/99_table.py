'''
Author: fg
Date: 2023-08-03 13:47:56
LastEditors: fg
LastEditTime: 2023-08-03 13:54:32
Description: 九九乘法表
'''
for i in range(1,10):
  for j in range(1,i+1):
    print('{}*{}={}\t'.format(j,i,i*j), end='')
  # 这里打印是用来换行的
  print('--')