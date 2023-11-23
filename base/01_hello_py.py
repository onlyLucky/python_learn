#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Author: fg
Date: 2023-06-29 11:19:49
LastEditors: fg
LastEditTime: 2023-07-01 11:31:03
Description: content
'''
print('hello python!!!')
import sys; x = 'runner'; sys.stdout.write(x + '\n')
# raw_input("按下 enter 键退出，其他任 意键显示...\n")
if True:
  print ("True")
else:
  print ("False")

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
str='123456789'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + 'hello')         # 连接字符串
 
print('------------------------------')

print('hello \nworld')
print(r'hello \n world')

# 数字类型
print('------------------------------')
a, b, c, d = 20, 5.5, True, 4+3j

print(type(a), type(b), type(c),type(d))

print(isinstance(a,int))

del a,b,c,d,str

# 数值运算
print(5+4)                  # 9 加法
print(4.3 - 2)              # 2.3 减法
print(3 * 7)                # 21 乘法
print(2/ float(4))          # 0.0 除法，得到一个浮点数 Python 2中的整数除法会直接舍弃小数部分
print(2 // 4)               # 0 除法，得到一个整数
print(17 % 3)               # 2 取余
print(2 ** 5)               # 32 乘方


# 比较运算符
a , b = True,False
print('2 < 3: ', 2 < 3)
print('2 == 3: ', 2 == 3)

# 逻辑运算符
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# 类型转换
print(int(a))   # 1
print(float(b)) # 0.0
print(str(a))   # "True"

# List（列表）
# 变量[头下标:尾下标]
list = [ 'abcd', 786 , 2.23, 'python', 70.2 ]
tempList = [123, 'runner']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tempList * 2)    # 输出两次列表
print (list + tempList) # 连接列表

# 列表数据更改

a = [1, 2, 3, 4, 5, 6]
print(a)
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)

def reverseWords(input):
  inputWords = input.split(' ')
  inputWords = inputWords[-1::-1]
  output = ' '.join(inputWords)
  return output

if __name__ == "__main__":
  input = 'hello world python'
  rw = reverseWords(input)
  print(rw)


print("-------------Tuple--------------")
# Tuple（元组）
tuple = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tempTuple = (123, 'python')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tempTuple * 2)     # 输出两次元组
print (tuple + tempTuple) # 连接元组

""" 
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。 
"""
# Set（集合）

print("-------------Set--------------")

sites = {'java', 'python', 'vue', 'go', 'react', 'c++'}
print(sites)   # 输出集合，重复的元素被自动去掉

if 'pythons' in sites:
  print('pythons in')
else:
  print('pythons not in')

a = set('javascript')
b = set('java')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素


# Dictionary（字典）
print("-------------Dictionary--------------")

dict = {}
dict['one'] = "1 - one"
dict[2]     = "2 - targe"

tempDict = {'data': 'python','code':1, 'msg': 'hello world'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tempDict)          # 输出完整的字典
print (tempDict.keys())   # 输出所有键
print (tempDict.values()) # 输出所有值

""" 
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""

# bytes 类型
print("-------------bytes--------------")
x = bytes("hello", encoding="utf-8")
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b" world"  # 拼接操作，得到 b"hello world"
print(x,y,z)



