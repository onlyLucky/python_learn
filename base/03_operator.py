'''
Author: fg
Date: 2023-07-03 16:53:06
LastEditors: fg
LastEditTime: 2023-07-05 10:24:34
Description: 03.运算符
'''

# 算术运算符
# + - * / % 基础运算符和其他编程语言一致，

print(4//2)        
print(2**3)

# 比较运算符
# == != > < >= <= 和其他编程语言一致；

# 赋值运算符
# += -= *= /= %= 
a = 2
b = 3
a**=b
print(a) 
a//=b
print(a) 

a="hello world!!!!!"
print(len(a))

if (n:=len(a))>10:
  print(f"list is too long ({n} elements, expected <= 10)")



print(bin(5))   

a = 60          # 60 = 0011 1100 
b = 13          # 13 = 0000 1101 
c = 0                   

print(a & b)    # 12 = 0000 1100 
print(a | b)    # 61 = 0011 1101 
print(a ^ b)    # 49 = 0011 0001
print(~a)       # -61 = 1100 0011
print(a << 2)   # 240 = 1111 0000
print(a >> 2)   # 15 = 0000 1111

# and or not

# in  not in












