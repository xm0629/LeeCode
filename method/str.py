"""
如果要把一个类的实例变成 str 就需要实现 __str__() 方法
"""

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def __str__(self):
        return ('(Person: %s, %s)' % (self.name, self.gender))

temp = Person('Bob', 'male')

print(temp)

