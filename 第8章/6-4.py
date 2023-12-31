"""
6-4 计数排序-Python
有一种简单的排序算法，叫做计数排序。这种排序算法对一个待排序的表进行排序，并将排序结果存放到另一个新的表中。必须注意的是，表中所有待排序的关键字互不相同，计数排序算法针对表中的每个记录，扫描待排序的表一趟，统计表中有多少个记录的关键字比该记录的关键字小。假设针对某一个记录，统计出的计数值为c，那么，这个记录在新的有序表中的合适的存放位置即为c。 编写实现计数排序的算法。

函数接口定义：
在这里描述函数接口。例如：
    def count_sort(a, b, n):
    # 计数排序算法，将包括 n 个数据的数组 a 中的记录排序后放⼊数组 b 中

输入样例：
在这里给出一组输入。例如：
    11 4 53 34 29 68

输出样例：
在这里给出相应的输出。例如：
    [11, 4, 53, 34, 29, 68]
    [4, 11, 29, 34, 53, 68]

@Author: FoskyM
@Date: 2023-12-31 15:01
"""

def count_sort(a, b, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if a[j] < a[i] and j != i:
                count += 1
        b[count] = a[i]
        count = 0


if __name__ == '__main__':
    data = [int(x) for x in input().split(' ')]
    print(data)

    n = len(data)

    result = [None] * n
    count_sort(data, result, n)

    print(result)