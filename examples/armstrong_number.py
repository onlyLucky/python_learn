'''
Author: fg
Date: 2023-08-03 14:11:54
LastEditors: fg
LastEditTime: 2023-08-03 14:21:17
Description: 阿姆斯特朗数 自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。（例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数）
'''

num = int(input("请输入一个数字："))

# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))

#检测
temp = num
while temp > 0:
  digit = temp%10
  sum += digit**n
  temp //= 10

# 输入结果
if num == sum:
  print(num,"是阿姆斯特朗数")
else:
  print(num,"不是阿姆斯特朗数")