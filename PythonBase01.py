import math

# 以下为数组处理方法
result = 10+29*39-24/8

print(result)

qq = not 1 < 2

print(qq)

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print(len(week))

week.append('Saturday')

print(week)

week.insert(6, 'Sunday')

print(week)

list.reverse(week)

print(week)

list.sort(week)

print(week)

week.append(1)

print(week)

list_empty = [None]*10

print(list_empty)

eightJZ = 0o10
print(eightJZ)

print(math.pi)
# 查看包内容
print(dir(math))

# encode转义方法应用
name = '恭喜'.encode()

# format方法应用
age = 20
name = 'killua'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 对于浮点数‘0.333’保留小数点（.）后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用（^）定义'__hello__'字符串长度为11
print('{0:^11}'.format('hello'))

# 通过end制定结尾
print('a', end='')
print('b', end=' hehe\n')
