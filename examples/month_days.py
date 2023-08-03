'''
Author: fg
Date: 2023-08-03 17:14:40
LastEditors: fg
LastEditTime: 2023-08-03 17:21:09
Description: 计算每个月天数
'''

import calendar
monthRange = calendar.monthrange(2023,8)
print(monthRange)

# (1, 31) 输出的意思为 2023 年 8 月份的第一天是星期二，该月总共有 31 天。第一个元素是所查月份的第一天对应的是星期几（0-6）