'''
Author: fg
Date: 2023-08-03 14:23:57
LastEditors: fg
LastEditTime: 2023-08-03 14:33:44
Description: 十进制转二进制、八进制、十六进制
'''

dec = int(input('输入数字：'))

print("十进制数为：",dec)
print("转换为二进制为：",bin(dec))
print("转换为八进制为：",oct(dec))
print("转换为十六进制为：",hex(dec))

# 二进制转换实例
binary_number = '101010'
decimal_number = int(binary_number,2) # 二进制转换为十进制
octal_number = oct(decimal_number)      # 十进制转换为八进制
hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制

print('二进制数:', binary_number)
print('转换为十进制:', decimal_number)
print('转换为八进制:', octal_number)
print('转换为十六进制:', hexadecimal_number)

octal_number = '52'
decimal_number = int(octal_number, 8)      # 八进制转换为十进制
binary_number = bin(decimal_number)         # 十进制转换为二进制
hexadecimal_number = hex(decimal_number)    # 十进制转换为十六进制

print('八进制数:', octal_number)
print('转换为十进制:', decimal_number)
print('转换为二进制:', binary_number)
print('转换为十六进制:', hexadecimal_number)

hexadecimal_number = '2a'
decimal_number = int(hexadecimal_number, 16)   # 十六进制转换为十进制
binary_number = bin(decimal_number)             # 十进制转换为二进制
octal_number = oct(decimal_number)              # 十进制转换为八进制

print('十六进制数:', hexadecimal_number)
print('转换为十进制:', decimal_number)
print('转换为二进制:', binary_number)
print('转换为八进制:', octal_number)