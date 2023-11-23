# 数据类型转换 显式类型转换 隐式类型转换

# 隐式类型转换

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

# 整型和字符串类型运算结果会报错 11+'123';输出 TypeError

# 显式类型转换

intX = int(1)                  # 1
intY = int(2.8)                # 2
intZ = int("3")                # 3

floatX = float(1)              # 1.0
floatY = float(2.8)            # 2.8     
floatZ = float("3")            # 3.0
floatW = float("4.2")          # 4.2

strX = str("say")              # "say"
strY = str(2)                  # "2"
strZ = str(3.0)                # "3.0"

