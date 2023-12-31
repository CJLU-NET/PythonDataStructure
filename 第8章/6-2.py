"""
6-2 正负排序-Python
编写算法，对 n 个关键字取整数值的记录序列进行整理，以使所有关键字为负值的记录
排在关键字为非负值的记录之前，要求：
① 采用顺序存储结构，至多使用⼀个记录的辅助存储空间；
② 算法的时间复杂度为 O(n)
提示：借助快速排序中⼦表划分的算法思想对表中的数据进行划分。

函数接口定义：
在这里描述函数接口。例如：
    def process(a, n):
    # 对数组 a 中的 n 个关键字进⾏整理
    # 使所有关键字为负值的记录排在关键字为⾮负值的记录之前

输入样例：
在这里给出一组输入。例如：
    1 -2 3 -4 5

输出样例：
在这里给出相应的输出。例如：
    [1, -2, 3, -4, 5]
    [-4, -2, 3, 1, 5]

@Author: FoskyM
@Date: 2023-12-31 14:23
"""

def process(a, n):
    low = 0
    high = n - 1
    while low < high:
        while a[low] < 0:
            low += 1
        while a[high] > 0:
            high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

if __name__ == '__main__':

    data = [int(x) for x in input().split(' ')]

    n=len(data)
    print(data)
    process(data,n)
    print(data)