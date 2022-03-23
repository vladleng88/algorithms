"""
Lesson 8.  Recursion. Continuation
"""
import numpy as np
#import sys
import test1
from lesson7 import recursion_factorial

#print(sys.modules.keys())
#print( 'test1' in sys.modules.keys())
s = test1.t1.sum_ab(1,2)
#print(s)
#print(dir(test1.t1))
def recursion_generate_numbers(n, m):
    """
    Функция по генерации возможных последовательностей длиной n из m чисел
    Их количество должно быть равно n**m
    :param n: длина строки
    :param m: число цифр от 0 до m-1
    :return: Список из всевозможных последовательностей длиной n из m чисел
    """
    def generate_numbers(n, m, prefix=''):
        if n==0:
            res.append(prefix)
            return
        for i in range(m):
            prefix+=str(i)
            generate_numbers(n-1, m, prefix)
            prefix = prefix[:-1]
    res = []
    generate_numbers(n,m)
    print('len=', len(res), '\n res:', np.array(res))
def recursion_generate_permutation(n,m):
    """
    Функция для нахождения всех перестановок m чисел в n позициях
    :param n: длина последовательности чисел
    :param m: числа последовательности от 0 до m-1
    :return: Спсиок возможных перестановок m чисел. Число всех перестановок равно m!
    """
    def generate_permutation(n, m, prefix = ''):
        if n==0:
            res.append(prefix)
        for i in range(m):
            if str(i) in prefix:
                continue
            prefix+=str(i)
            generate_permutation(n-1, m,prefix)
            prefix = prefix[:-1]
    res = []
    generate_permutation(n,m)
    print('m!={0}\nlen_res = {1}, res: {2}'.format(recursion_factorial(m),len(res), res))

#recursion_generate_numbers(5, 2)
recursion_generate_permutation(4, 4)