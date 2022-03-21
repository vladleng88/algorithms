"""
Lesson 4. "Функции"
is_simple_number(a)
factorize_number(a)
"""
def is_simple_numder(a):
    """
    Функция по определению простое или сосотавное число a
    :param a: Любое исследуемое число
    :return: True или False
    """
    divesor=2
    while divesor<a:
        if a%divesor==0:
            return False
        divesor+=1
    return True
print(is_simple_numder(9))
def factorize_number(a):
    """
    Функция раскладывает число на мноджители и печатает их на экран
    :param a: раскладываемое число
    :return: простые множители
    """
    divisor = 2
    res = []
    while a > 1:
        if a%divisor==0:
            print(divisor)
            res.append(divisor)
            a //= divisor
        else:
            divisor += 1
    return res
print(factorize_number(11))