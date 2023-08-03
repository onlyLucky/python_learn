'''
Author: fg
Date: 2023-08-03 09:23:17
LastEditors: fg
LastEditTime: 2023-08-03 09:32:43
Description: 随机数生成
'''
import random

random_number = random.random()
print('生成一个介于 0.0 和 1.0 之间的随机小数{0}'.format(random_number))

random_randint = random.randint(0,9)
print('生成 0 ~ 9 之间的随机整数{0}'.format(random_randint))

list = [1,2,3,4,5]
random_element = random.choice(list)
print('生成从序列中随机选择一个元素{0}'.format(random_element))

random.shuffle(list)
print('序列中的元素进行随机排序{0}'.format(list))