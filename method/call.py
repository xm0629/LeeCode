"""
__call__ 函数其实是一个对象, 也可以调用, 所有的函数都是可调用对象.
"""

# 把 Person 变成为可调用的对象

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
       print('My name is %s...' %(self.name)) 
       print('My friend is %s ...' %(friend))


tmp = Person('Bob', 'male')
print(tmp)
tmp('Rose')

class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        a, b = 0, 1
        self.l = []

        for i in range(num):
            self.l.append(a)
            a,b = b, a+b
        return self.l

    def __str__(self):
        return str(self.l)

    __rept__ = __str__

f = Fib()
print(f(10))
        
