import hashlib
# message='hello world'
# md5=hashlib.md5(message.encode())
# print(message,md5.hexdigest())
#
# class User:
#     def __init__(self,username,password):
#         self.username= username
#         md5= hashlib.md5(password.encode())
#         self.password = md5.hexdigest()
#     def check_password(self,password):
#         md5= hashlib.md5(password.encode())
#         if self.password == md5.hexdigest():
#             return 'ture'
#         else:
#             return 'flase'
# user=User('xiao1995',"123456")
# print(user.check_password('123'))
# print(user.check_password('123456'))


def md5(content):
    return hashlib.md5(content.encode()).hexdigest()
password="xiao1992"
res=md5(password)
print(password)
print(res)