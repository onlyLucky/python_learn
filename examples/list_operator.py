'''
Author: fg
Date: 2023-08-03 17:28:48
LastEditors: fg
LastEditTime: 2023-08-03 19:43:11
Description: list 常用操作
'''
# 1.list 定义
li = ['a','b','c','d','e','f','g','h']
li[1]                                 # b

# 2.list 负数索引
li[-1]                                # h
li[-3]                                # f
li[1:-1]                              # ['b','c','d','e','f','g']
li[0:3]                               # ['a','b','c']

# 3.list 增加元素
li.append('i')                        # li: ['a','b','c','d','e','f','g','h','i']
li.insert(2,'insert')                 # li: ['a','b','insert','c','d','e','f','g','h','i']
li.extend(['extend1','extend2'])      # li: ['a','b','insert','c','d','e','f','g','h','i','extend1','extend2']

# 4.list 搜索    index list 中没有找到值, Python 会引发一个异常
li.index('insert')                    # 2
'pp' in li                            # False
'extend1' in li                       # True

# 5.list 删除元素   remove list 中没有找到值, Python 会引发一个异常
li.remove("g")                        # li: ['a','b','insert','c','d','e','f','h','i','extend1','extend2']
li.pop()                              # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。li: ['a','b','insert','c','d','e','f','h','i','extend1']

# 6.list 运算符
li = ['a', 'b', 'c']
li = li + ['example', 'new']          # li: ['a', 'b', 'c','example', 'new']
li += ['two']                         # li: ['a', 'b', 'c','example', 'new','two']
li = [1, 2] * 3                       # li: [1, 2,1, 2,1, 2]

# 7.使用join链接list成为字符串
params = {"server":"python", "database":"master", "uid":"sa", "pwd":"secret"}
["%s=%s" % (k, v) for k, v in params.items()] # ['server=python', 'uid=sa', 'database=master', 'pwd=secret']
";".join(["%s=%s" % (k, v) for k, v in params.items()]) # 'server=python;uid=sa;database=master;pwd=secret'

# 8.list 分割字符串
li = ['server=python', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)                      # s:'server=python;uid=sa;database=master;pwd=secret'
s.split(";")                          # ['server=python', 'uid=sa', 'database=master', 'pwd=secret']
s.split(";", 1)                       # ['server=python', 'uid=sa;database=master;pwd=secret']

# 9.list 的映射解析
li = [1, 9, 8, 4]
[elem*2 for elem in li]               # [2, 18, 16, 8]

# 10.dictionary 中的解析
params = {"server":"python", "database":"master", "uid":"sa", "pwd":"secret"}
params.keys()                         # ['server', 'database', 'uid', 'pwd']
params.values()                       # ['python', 'master', 'sa', 'secret']
params.items()                        # [('server', 'python'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')]
[k for k, v in params.items()]        # ['server', 'database', 'uid', 'pwd']
[v for k, v in params.items()]        # ['python', 'master', 'sa', 'secret']
["%s=%s" % (k, v) for k, v in params.items()]   #['server=python', 'database=master', 'uid=sa', 'pwd=secret']

# 11.list 过滤
li = ["a", "python", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]# ['python', 'foo']
[elem for elem in li if elem != "b"]  # ["a", "python", "foo", "c", "d", "d"]
[elem for elem in li if li.count(elem) == 1] # ["a", "python", "foo", "c"]