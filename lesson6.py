"""
lesson 6. Квадратичные сортировки
insert_sort() - сортировка методом вставки
choice_sort() - сортировка методов выбора
bubble_sort() - сортирвка методом пузырька
"""
def insert_sort(A):
    """
    Алгоритм сортировки методом вставки
    :return:
    """
    N = len(A)
    #sorted = [0]*N
    for i in range(1,N):
        for j in range(i, 0, -1):
            if A[j]<A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
def choice_sort(A):
    """
    Алгоритм сортировки методом выбора
    :return:
    """
    N = len(A)
    for i in range(N-1):
        for j in range(i, N):
            if A[j]<A[i]:
                A[i], A[j] = A[j], A[i]
def bubble_sort(A):
    """
    Алгоритм сортировки методом пузырька
    :return:
    """
    #A=[6,3,8,33,6,78,4,2,5]
    N = len(A)
    for i in range(N-1):
        for j in range(0, N-1-i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
def test_insert_sort():
    A = [1,5,6,7,8,3,2]
    insert_sort(A)
    if A == [1,2,3,5,6,7,8]:
        print('test-OK')
    else:
        print('test - Failed')
def test_choice_sort():
    A = [1, 5, 6, 7, 8, 3, 2]
    choice_sort(A)
    print(A)
    if A == [1, 2, 3, 5, 6, 7, 8]:
        print('test-OK')
    else:
        print('test - Failed')
def test_bubble_sort():
    A=[6,3,8,33,6,78,4,2,5]
    bubble_sort(A)
    print(A)
    if A==[2,3,4,5,6,6,8,33,78]:
        print('test - OK!')
    else:
        print('test - Failed')


test_bubble_sort()
test_insert_sort()
test_choice_sort()