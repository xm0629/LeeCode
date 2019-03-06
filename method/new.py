"""
1. 继承 object 的新式类才有 __new__.
2. __new__ 至少要有一个参数 cls, 代表当前类, 此参数在实例化时由 python解释器自动识别.
3. __new__ 必须要有返回值, 返回实例化出来的实例, 这点在实现 __new__时特别要注意, 可以 return 父类通过super(当前类名,
cls)）__new__出来的实例，或者直接是object的__new__出来的实例.
4.__init__有一个参数self，就是这个__new__返回的实例, __init__在__new__的基础上可以完成一些其它初始化的动作, __init__不需要返回值.
5.如果__new__创建的是当前类的实例, 会自动调用__init__函数, 通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例, 
如果是其他类的类名；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数.
"""


#class ATest(object):
#    def __init__(self, *args, **kwargs):
#        print("init A")
#
#    def __new__(cls, *args, **kwargs):
#        print("new A %s" % cls)
#        #return super(ATest, cls).__new__(cls, *args, **kwargs)
#        return object.__new__(cls, *args, **kwargs)
#
#
#temp = ATest()
#print(temp)

class Person(object):
    def __new__(cls, name, age):
        print("__new__called.")
        return super(Person, cls).__new__(cls)
        #return object.__new__(cls, name, age)

    def __init__(self, name, age):
        print("__init__.called.")
        self.name = name
        self.age = age

    def __str__(self):
        return ('<Person: %s(%s)>' % (self.name, self.age))

tmp = Person('Bob', 24)
print(tmp)

"""
什么时候需要使用 __new__
new 方法主要是当你继承一些不可变的 class 时 (比如 int, str, tuple)
提供给你一个自定义这些类的实例化途径, 还有就是定义的 metaclass
"""

# 假如我们需要一个永远都是正整数的整数类型



#class Positive(int):
#    def __init__(self, value):
#        super(Positive, self).__init__(abs(value))
#
#tmp1 = Positive(-3)
#print(tmp1)


class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


tmp2 = PositiveInteger(-3)
print(tmp2)




# 实现单例, 也就是每次实例化时只返回同一个实例对象

class SingleObject(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):# 先判断是否已有实例, 保证单例.
            cls.instance = super(SingleObject, cls).__new__(cls)
        return cls.instance

obj = SingleObject()
obj1 = SingleObject()

obj.attr = 'value'
print(obj.attr, obj1.attr)
print(obj is obj1)










