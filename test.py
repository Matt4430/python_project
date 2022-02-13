




class A(object):
    a = 'a'

    @staticmethod
    def foo1(name):  # 静态函数
        print("hello", name)

    def foo2(self, name):  # 常规函数
        print("hello", name)

    @classmethod
    def foo3(cls, name):  # 类方法
        print("hello", name)

#接着我们实例化A类
a = A()

a.foo1('ma')  # output:hello ma
A.foo1('ma')  # output:hello ma

'''
而foo2是常规函数，只能通过类的实例化来调用，即a.foo2()来调用。
'''
a.foo2('杨晓东') # output:hello 杨晓东

'''
而foo3是类函数，cls作为第一个参数用来表示类本身，在类方法中用到，类方法只是与类本身有关而与实例无关的方法。
可以通过实例化来调用，也可以通过  类名.类函数名  来调用。
即  a.foo3('mam')  或  A.foo3('mam')
'''
a.foo3('mam')  # output:hello mam
A.foo3('mam')  # output:hello mam

