"""
6-1 双栈-Python

将编号为 0 和 1 的两个栈存放于⼀个数组空间 V[m]中，栈底分别处于数组的两端。
当 第 0 号栈的栈顶指针 top[0]等于-1 时该栈为空；当 第 1 号栈的栈顶指针 top[1]等于 m 时，该栈为空。
两个栈均从两端向中间增⻓（⻅图 3.18）。  ### 勘误：图 3.18 应为图 3.19
试编写双栈初始化，判断栈空、栈满、进栈和出栈 等算法的函数。

函数接口定义：
    双栈数据结构的定义如下：
    Class DblStack:  ### 勘误：应为小写 class
        top, bot = [None, None], [None, None] # 栈顶和栈底指针
        V = [] # 栈数组
        m = None # 栈最⼤可容纳元素个数
        __init__(self): # 双栈初始化  ### 勘误：函数定义要有 def
            pass
        dbl_push(self, e): # 把元素 e 进栈
            pass
        dbl_pop(self): # 出栈
            pass
        dbl_empty(self): # 判断栈空
            pass
        dbl_full(self): # 判断栈满
            pass

@Author: FoskyM
@Date: 2023-10-24 19:42
"""


class DblStack:
    top, bot = [None, None], [None, None]  # 栈顶和栈底指针
    V = []  # 栈数组
    m = None  # 栈最⼤可容纳元素个数

    def __init__(self, size):  # 双栈初始化
        self.m = size
        self.V = [None] * self.m
        self.top = [-1, self.m]
        self.bot = [0, self.m - 1]

    def dbl_push(self, e, d):  # 把元素 e 进栈
        if self.dbl_full():
            print('Stack is full!')
            return

        if d == 0:
            self.top[0] += 1
            self.V[self.top[0]] = e
        else:
            self.top[1] -= 1
            self.V[self.top[1]] = e

    def dbl_pop(self, d):  # 出栈
        if self.dbl_empty():
            print('Stack is empty!')
            return

        if d == 0:
            if self.top[0] == -1:
                return
            e = self.V[self.top[0]]
            self.top[0] -= 1
            return e
        else:
            if self.top[1] == self.m:
                return
            e = self.V[self.top[1]]
            self.top[1] += 1
            return e

    def dbl_empty(self):  # 判断栈空
        return self.top[0] == -1 and self.top[1] == self.m

    def dbl_full(self):  # 判断栈满
        return self.top[0] + 1 == self.top[1]

    def show(self):
        for i in range(self.m):
            if self.V[i] is not None:
                print(self.V[i], end=' ')
        print()


if __name__ == '__main__':

    # 输入双栈容量c

    c = int(input())

    ds = DblStack(c)
    for i in range(c):
        j = i % 2
        print(i, end=' ')
        ds.dbl_push(i, j)
    print()

    ds.show()

    for i in range(c):
        j = i % 2
        print(ds.dbl_pop(j), end=' ')
    print()
