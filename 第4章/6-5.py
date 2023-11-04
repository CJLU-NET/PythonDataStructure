"""
6-5 判断数组中是否有相同元素-Python
设二维数组a[1..m, 1..n] 含有m*n 个整数。写一个算法判断a中所有元素是否互不相同?输出相关信息(yes/no)。

函数接口定义：
# 判断⼆维数组中 a 所有元素是否互不相同，如是，返回 True；否则，返回 False
def is_equal(a, m, n):

@Author: FoskyM
@Date: 2023-11-04 08:09
"""

def is_equal(a, m, n):
    # 使用列表解析解构为一维数组
    b = [item for row in a for item in row]

    for i in range(m * n):
        for j in range(i + 1, m * n):
            if b[i] == b[j]:
                return False
    return True

if __name__ == '__main__':

    m = int(input())
    n = int(input())

    a = []
    for i in range(m):
        c = [int(x) for x in input().split(' ')]
        a.append(c)
    if is_equal(a, m, n):
        print('yes')
    else:
        print('no')