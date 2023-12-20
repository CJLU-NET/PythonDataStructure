"""
6-1 折半查找-递归实现-Python

函数接口定义：
在这里描述函数接口。例如：
    def bin_srch(self, key, low, high):
    # 在⻓为 n 的有序表中查找关键字 k，若查找成功，返回 k 所在位置，查找失败返回 0。

输入样例：
在这里给出一组输入。例如：
    5
    10
    20
    30
    40
    50
    50

输出样例：
在这里给出相应的输出。例如：
    该关键字位于第5个位置。

@Author: FoskyM
@Date: 2023-12-20 15:56
"""

class ElemType:
    def __init__(self, key, otherinfo=""):
        self.key = key  # 关键字域
        self.otherinfo = otherinfo  # 其他域


class SSTable:
    def __init__(self):
        self.r = [ElemType(0)]  # 存储空间基地址，r[0]闲置不用
        self.length = 0  # 当前长度

    def create_st(self, n):
        # 创建顺序表
        self.length = n  # 定义顺序表的长度为n
        for i in range(n):  # 依次插入关键字
            self.r.append(ElemType(int(input())))

    def search_bin(self, key):
        # 算法7.3 折半查找
        low = 1
        high = self.length  # 置查找区间初值
        while low <= high:
            mid = (low + high) // 2
            if key == self.r[mid].key:
                return mid  # 找到待查元素
            elif key < self.r[mid].key:
                high = mid - 1  # 继续在前一子表进行查找
            else:
                low = mid + 1  # 继续在后一子表进行查找
        return 0  # 表中不存在待查元素

    def bin_srch(self, key, low, high):
        if low <= high:
            mid = (low + high) // 2
            if key == self.r[mid].key:
                return mid
            elif key < self.r[mid].key:
                return self.bin_srch(key, low, mid - 1)
            else:
                return self.bin_srch(key, mid + 1, high)
        else:
            return -1

if __name__ == '__main__':
    st = SSTable()  # 初始化顺序表
    n = int(input())
    st.create_st(n)  # 创建顺序表
    key = int(input())
    locate = st.bin_srch(key, 1, n)  # 利用折半查找在顺序表中查找该关键字的位置
    if locate == -1:
        print("未找到该关键字！")
    else:
        print("该关键字位于第{}个位置。".format(locate))