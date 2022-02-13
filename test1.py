


class A(object):
    a = 'a'

    @staticmethod
    def foo1(name):
        print('hello', name)

        """
        print(A.a)   # 正常
        print(A.foo2('杨晓东2'))   #  因为没有实例化类   报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)
        """


    def foo2(self, name):
        print('hello', name)

    @classmethod
    def foo3(cls, name):
        print('hello', name)
        print(cls().foo2('杨晓东'))  # 可以在foo3中调用foo2，因为持有cls参数，彷佛是类本身，故可以调用该foo2方法。

print(A.a)              # output:a

print(A.foo3('杨晓东3'))  # output:hello 杨晓东3
                         # output:hello 杨晓东

B = A()
print(B.foo2('杨晓东2'))  # output:hello 杨晓东2     普通类方法，实例化后正常调用&输出

print(A.foo2('杨晓东22'))  # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)

