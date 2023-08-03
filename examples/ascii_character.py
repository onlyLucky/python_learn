'''
Author: fg
Date: 2023-08-03 14:40:45
LastEditors: fg
LastEditTime: 2023-08-03 15:36:40
Description: ASCII码与字符相互转换
'''

c = input("请输入一个字符：")

# 用户输入ASCII码，并将输入的数字类型转为整形
a = int(input("请输入一个ASCII码："))

print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))