from test1.t1 import *
from test1 import *
from test1 import t2
from dataclasses import dataclass
class C:
    """class desciption"""
    def __init__(self):
        self.b = 20
        self._c = 30
    #def __getattribute__(self, item):
    #    print('get item = ', item)
    #    return object.__getattribute__(self, item)
    #def __setattr__(self, key, value):
    #    print('set attr :', key)
    #    self.__dict__[key] = value
    @staticmethod
    def func(y, x):
        return x+y
    a = 10
    def method1(self):
        return self.b
c1 = C()
#print(c1.__dict__)
print('staticmethod call...', C.func(10,10))
print(c1.a)
print(c1.b)
print(c1._c)
c1.b = 200
print(c1.b)
print('dir',dir(C))
print('__dict__',C.__dict__)

from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @abstractmethod
    def func_abs(self, x):
        pass
class B(A):
    def __init__(self, x):
        self.x = 10
    def __str__(self):
        return str(self.x)+'---'
    def __repr__(self):
        return str(self.x)+'sadasdasd'
    def __add__(self, other):
        return self.x+other
    def __iadd__(self, other):
        return self.x+other
    def func_abs(self, x):
        print(x)
bb = B(A)
bb.func_abs(7)
print(bb)
c = bb+5
print(c)
bb+=10
print(bb)
class Test():
    def __init__(self):
        self.__x = 10
        self.__y = 20
    def getX(self):
        return self.__x
    def setX(self, value):
        self.__x = value
    def delX(self):
        del self.__x
    v = property(getX,setX, delX, 'sadsad')
t = Test()
t.v = 35
print('x', t.getX())
t.delX()
print(t.__dict__)
print('----------class Test2---------')
class Test2():
    def __init__(self):
        self.__x = 10
        self.__y = 20
    @property
    def xp(self):
        return self.__x
    @xp.setter
    def xp(self, value):
        self.__x = value
    @xp.deleter
    def xp(self):
        del self.__x
    xx: str = 'annodfsdft'
t = Test2()
print(t.__annotations__['xx'].__getattribute__)
print('x', t.xp)
t.xp = 35
print('x', t.xp)
del t.xp
print(t.__dict__)
ss = 4
vars(t)
def gs():
    global ss
    ss+=4
gs()
print(ss)

@t2.testdeco
def testFunc():
    print('testFunc work')
    return 1
#print('testFunc call...', testFunc())

class C0:
    def __init__(self):
        self.__data = {}
        #self.__name = name
    def getData(self):
        return self.__data
    def setData(self, key, value):
        self.__data[key] = value


class C1(C0):
    def __init__(self):
        super(C1, self).__init__()
        self.__data = 0
    def getData2(self):
        return self.__data
    def setData2(self, data):
        self.__data = data
c1 = C1()
c1.setData2(1)
print('data_1', c1.getData2())
print('data_0', c1.getData())
c1.setData(1,1)
print('data_1', c1.getData2())
print('data_0', c1.getData())
def testfunction(a:int, b:int):
    return a+b
rst = testfunction(1., 2)
print(rst)
@dataclass
class DC:
    a: str = 1
    b: float = '2'
    c: str = '3'
    #def __init__(self, f):
    #    self.f = f
    def tst(self):
        return self
dc1 = DC(c=11, b=12,a=13)
print(dc1.__annotations__)
print('__dict__',dc1.__dict__)
print('vars dc1',vars(dc1))
print(dc1)
print(dc1.a)

print('dir DC',dir(DC))
print('vars DC',vars(DC))
print('dir dc1',dir(dc1))
#print('dict',__dict__(DC))
print( hasattr(DC, 'f'))



a = {'a': 1, 'b':2}
print(a.items())