__all__ = ['sum_ab', 'testdeco']

def sum_ab(a,b):
    return a+b
def testdeco(func):
    print('work in decoration')
    return func
def testdeco2(func):
    print('work in decoration2')
    return func