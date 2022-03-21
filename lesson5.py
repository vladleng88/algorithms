"""
lesson 5. Массивы
array_search()
invert_array(A)
left_shift()
right_shift()
"""

def array_search(listt, a):
    """
    Функция осуществляет поиск числа a в массиве list
    Если число a есть в массиве, то возвращает индекс элемента,
    если нет - то -1.
    :return: индекс элемента а или -1
    """
    for i in range(len(listt)):
        if listt[i]==a:
            return i
    return -1
def invert_array(A):
    """
    Функция для обращения списка А
    :param A:
    :return: список со значениями в обратном порядке
    """
    N = len(A)
    for i in range(N//2):
        A[i], A[N-1-i] = A[N-1-i], A[i]
def left_shift(A):
    tmp = A[0]
    N = len(A)
    for i in range( N-1):
        A[i] = A[i+1]
    A[N-1] = tmp
def right_shift(A):
    N = len(A)
    tmp = A[-1]
    for i in range(N-1, 0, -1):
        A[i] = A[i-1]
    A[0] = tmp

def test_invert_array():
    """
    Функция для тестирования функции invert_array
    :return:
    """
    print("start testing invert_array function...")
    A = [3,5,8,2,5,8,4]
    invert_array(A)
    B = [4, 8, 5, 2, 8, 5, 3]
    key = True
    for i in range(len(A)):
        if A[i]!=B[i]:
            key = False
            break
    print('test - OK') if key else print('test -  Failed')
def test_array_search():
    """
    Функция для тестирования функции array_search
    :return:
    """
    print("start testing array_search function...")
    A = [1, 2,3,4,5,6]
    if array_search(A, 4)==3:
        print('test-Ok')
    else:
        print('test - Failed')
    A = [-1, 20, 7, -8, -5, 6]
    if array_search(A, -5)==4:
        print('test-Ok')
    else:
        print('test - Failed')
def test_array_shift():
    A = [3,6,8,1,3,5,4,2]
    left_shift(A)
    B = [3,6,8,1,3,5,4,2]
    right_shift(B)
    A_left_shift = [6,8,1,3,5,4,2,3]
    B_right_shift = [2,3,6,8,1,3,5,4]
    key_lshift = True
    for i in range(len(A)):
        if A[i] != A_left_shift[i]:
            key_lshift = False
            break
    print('test left shift OK') if key_lshift else print('test left_shift - Failed')
    key_rshift = True
    for i in range(len(B)):
        if B[i] != B_right_shift[i]:
            key_rshift = False
            break
    print('test right shift OK') if key_rshift else print('test right_shift - Failed')
test_array_search()
test_invert_array()
test_array_shift()