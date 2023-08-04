'''
Author: fg
Date: 2023-08-04 10:04:35
LastEditors: fg
LastEditTime: 2023-08-04 10:14:17
Description: 秒表功能
'''
import time

print('按下回车开始计时，按下Ctrl+C 停止计时')
while True:
  input("")   # 如果是 python 2.x 版本请使用 raw_input()
  start_time = time.time()
  print('开始')
  try:
    while True:
      print('计时：', round(time.time() - start_time,0), '秒')
      time.sleep(1)
  except KeyboardInterrupt:
    print('结束')
    end_time = time.time()
    print('总共的时间为：', round(end_time-start_time,2),'秒')
    break