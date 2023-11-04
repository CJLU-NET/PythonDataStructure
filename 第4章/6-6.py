"""
6-6 正负分类-Python
设任意n个整数存放于数组A(1:n)中，试编写算法，将所有正数排在所有负数前面（要求算法复杂度为0(n)）。

函数接口定义：
# 数组 A 中存储 n 个整数，将 A 中所有正数排在所有负数的前⾯
def partition(A, n):

输入样例：
5
1 -1 2 -2 3

输出样例：
1 3 2 -2 -1

@Author: FoskyM
@Date: 2023-11-04 08:18
"""

def partition(A, n):
    i = 0
    j = n - 1
    while i < j:
        while A[i] > 0:
            i += 1

        while A[j] < 0:
            j -= 1

        if i < j:
            x = A[i]
            A[i] = A[j]
            A[j] = x

# python 语法糖真的好用
# 不过根据输出样例的顺序，上面首尾指针的方法才能满足题意
# def partition(A, n):
#     # 使用列表解析解构为一维数组
#     b = [item for item in A if item > 0] + [item for item in A if item < 0]
#     for i in range(n):
#         A[i] = b[i]

if __name__=='__main__':

    n = int(input())
    a =[ int(x) for x in input().split(' ')]

    partition(a,n)
    for i in range(n):
        print(a[i],end=' ')
    print(end='\n')