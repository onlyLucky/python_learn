'''
Author: fg
Date: 2023-08-06 17:24:12
LastEditors: fg
LastEditTime: 2023-08-06 17:27:28
Description: 移除列表中重复的元素
'''
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1)))

print(list(set(list_1) ^ set(list_2)))