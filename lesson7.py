"""
Lesson 7. Рекурсия
recursion_recatangle()
"""
import graphics as gr
def recursion_recatangle():
    """
    Функция по рекурсивному (с помощью функици fractal_rectangle) рисованию прямоугольников
    :return:
    """
    win = gr.GraphWin('test window', 500, 500)
    def fractal_rectangle(A,B,C,D, deep=5):
        if deep<1:
            return
        for M,N in (A, B),(B,C), (C,D), (D,A):
            gr.Line(gr.Point(*M), gr.Point(*N)).draw(win)
        A2 = (A[0]*(1-alpha)+B[0]*alpha,A[1]*(1-alpha)+B[1]*alpha)
        B2 = (B[0]*(1-alpha)+C[0]*alpha,B[1]*(1-alpha)+C[1]*alpha)
        C2 = (C[0]*(1-alpha)+D[0]*alpha,C[1]*(1-alpha)+D[1]*alpha)
        D2 = (D[0]*(1-alpha)+A[0]*alpha,D[1]*(1-alpha)+A[1]*alpha)
        fractal_rectangle(A2,B2,C2,D2, deep-1)
    alpha = 0.1
    #c = gr.Line(gr.Point(50,50), gr.Point(100, 50)).draw(win)
    fractal_rectangle((100,100), (400,100), (400,400), (100,400), 10)
    win.getMouse() # Pause to view result
    win.close()
def recursion_factorial(N):
    """
    Функция для рекурсивного вычисления факториала числа
    :return:
    """
    def factorize_number(N):
        assert N>=0, 'Факториал не определен'
        if N<1:
            return 1
        return factorize_number(N-1)*N

    res = factorize_number(N)
#    print('Task1. {0}! = {1} '.format(N,res))
    return res
def recursion_gcd():
    """
    Функция для рекурсивного Наибольшего общего делителя
    :return:
    """
    def gcd(a,b):
        if a==b:
            return a
        if a>b:
            d = gcd(a-b, b)
        else:
            d = gcd(b-a, a)
        return d
    def gcd2(a,b):
        if b==0:
            return a
        else:
            d = gcd2(b, a%b)
        return d
    a = 28
    b = 2468
    print('Task2. Great common divisor of {0} and {1} is {2}'.format(a,b,gcd2(a,b)))
def recursion_power():
    """
    Функция по возведению числа в степень рекурентным способом
    :return:
    """
    def pow(a, b):
        if b==0:
            return 1
        if b % 2 == 0:
            a2 = a**2
            return pow(a2, b/2)
        return pow(a, b-1) * a
    a = 3
    p = 4
    res = pow(a, p)
    print('Task3. {} in power of {} is {}'.format(a, p, res))
def recursion_hanoi():
    """
    Решение задачки о ханойской башне
    :return:
    """
    def hanoi(n, i, k):
        """
        Рекурсивная функция по перекладыванию башенки с n деталями из стойки i в стойку k
        :param n:
        :param i:
        :param k:
        :return: None
        """
        if n==0:
            print("Move floor №{0} из {1} в {2}".format(n, i, k))
            return
        tmp = 6-i-k
        hanoi(n-1, i, tmp)
        print("Move floor №{0} из {1} в {2}".format(n, i, k))
        hanoi(n-1, tmp, k)
    height = 3
    start = 1
    stop = 3
    print('Task4. Hanoi building...{} floor, from {}-th  to {} -th position'.format(height, start, stop))
    hanoi(3,1,3)


#recursion_factorial(5)
#recursion_recatangle()
#recursion_gcd()
#recursion_power()
#recursion_hanoi()