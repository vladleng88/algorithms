"""
Lesson 9. Быстрые сортровки (Сортировки слиянием и Томи Хоара)
"""
def recursion_merge_sort(A):
    def merge_sort(A):
        if len(A)//2==0:
            return A
        ind = len(A)//2
        B = A[:ind]
        B2 = A[ind:]
        B = merge_sort(B)
        B2 = merge_sort(B2)
        C = merge(B, B2)
        return C

    def merge(A, B):
        i,j = 0, 0
        C = []
        while True:
            if i==len(A):
                C += B[j:]
                break
            elif j==len(B):
                C += A[i:]
                break
            else:
                if A[i]<B[j]:
                    C.append(A[i])
                    i+=1
                elif A[i]==B[j]:
                    C +=[A[i]]*2
                    i+=1
                    j+=1
                else:
                    C.append(B[j])
                    j+=1
        return C
    B = merge_sort(A)
    print(B)
def recursion_hoar(A):
    def hoar(A):
        if len(A)<=1:
            return
        barrier = A[0]
        L = [A[i] for i in range(len(A)) if A[i]<barrier]
        M = [A[i] for i in range(len(A)) if A[i]==barrier]
        R = [A[i] for i in range(len(A)) if A[i]>barrier]
        hoar(L)
        hoar(R)
        A_summ = L+M+R
        for i in range(len(A)):
            A[i]=A_summ[i]
    #A = [6,3,5,9]
    hoar(A)
    print(A)
recursion_merge_sort([2,6,3,9,4,5,0,6,777, 2,3,66,78,74,32,35,37,96,65,43,37])
recursion_hoar([2, 6, 3, 9, 4, 5, 0, 6,777,2,3,66,78,74,32,35,37,96,65,43,37])
