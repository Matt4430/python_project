# -*- coding:utf-8 -*-

# 简单模式：只包含循环，不包含判断筛选

# 常规写法
list_1 = []
for i in range(1,10):
    list_1.append(i)
print(list_1)


# 例子：
list_2 = [i for i in range(1,20)]
print(list_2)