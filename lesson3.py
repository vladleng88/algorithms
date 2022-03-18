"""
Схема Горнера для перевода из любой системы счисления в десятичную и из десятичной в любую
"""
def to_decimal(x, base=2):
    """
    Преобразовывает число x системы счисления с основанием base в десятичную
    :param x: Число для преобразования в десятичную систему счисления (строка)
    :param base: основание системы счисления преобразуемого числа
    :return: число в десятчной системе счисления
    """
    y = [0] * (len(x) + 1)
    for i in range(0, len(x)):
        y[i + 1] = y[i] * base + int(x[i])
    return y[-1]
def from_decimal(x, base=2):
    """
    Преобразовывает число x из десятичной системы счисления в систему счисления с основанием base
    :param x: Число для преобразования
    :param base: основание системы счисления преобразуемого числа
    :return: число в системе счисления с основанием base (строка)
    """
    y2 = ''
    while x > 0:
        digit = x % base
        x //= base
        y2 += str(digit)
    y2 = y2[::-1]
    return y2
def test_to_decimal():
    key = True
    if to_decimal('1234', base=5)==194:
        print('Test1 - OK')
    else:
        print('Test1 - Failed')
        key = False
    if to_decimal('01100101', base=2)==101:
        print('Test2 - OK')
    else:
        print('Test2 - Failed')
        key = False
    if to_decimal('054236412577', base=8) == int('054236412577', base=8):
        print('Test3 - OK')
    else:
        print('Test3 - Failed')
        key = False
    return key

def main():
    if not test_to_decimal():
        exit('Test is failed')

    print("Введите основание системы счисления")
    base = int(input())
    print("Введите число в {base}-ой системе счисления".format(base=base))
    x = input().strip()
    num = to_decimal(x, base=base)
    print('Ответ:', num)

    print("Введите основание новой системы счисления")
    base2 = int(input())
    y2 = from_decimal(num, base2)
    print('число {num} в {base}-ой системе счисления равно: {y}'.format(base=base2, num=num, y=y2))

if __name__ == '__main__':
    main()

"""a=[3,5]
b=a.copy()
print( a is b)
a[1] = 7
print( a is b)
print( a, b)
"""
