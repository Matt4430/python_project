
"""
redis 操作


"""

import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'root')  # 设置 name 对应的值
r.lpush('na',12,'love','heihei','xixi','haha')
print(r['name'])
print(r.get('na'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型

