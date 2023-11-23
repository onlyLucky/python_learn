'''
Author: fg
Date: 2023-08-03 16:40:08
LastEditors: fg
LastEditTime: 2023-08-03 16:40:14
Description: 文件 IO
'''

# 使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。
with open('test.txt','wt') as out_file:
  out_file.write('hello world!!!\nPython')

with open('test.txt','rt') as in_file:
  text = in_file.read()
print(text)