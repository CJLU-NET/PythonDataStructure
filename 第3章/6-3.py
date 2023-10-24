"""
6-3 键盘输入栈-Python
设从键盘输⼊⼀整数的序列：a1, a2, a3, …, an，试编写算法实现：⽤栈结构存储输⼊的整数，当 ai ≠ −1时，将 ai进栈；当 ai = −1 时，输出栈顶整数并出栈。算法应对异常情况（⼊栈满 等）给出相应的信息。

函数接口定义：
    在这里描述函数接口。例如：
    def in_out_s(s,a):

@Author: FoskyM
@Date: 2023-10-24 22:58
"""

max_size = 5


class SqStack:
    def __init__(self):
        # 初始化顺序栈
        self.elem = [None] * max_size  # 为顺序栈动态分配一个最大容量为max_size的数组空间
        self.top, self.base = 0, 0  # top和base都指向栈底元素在顺序栈中的位置，空栈
        self.stack_size = max_size  # stack_size置为栈的最大容量max_size

    def push(self, e):
        # 将元素压入栈
        if self.top - self.base == self.stack_size:  # 栈满
            raise Exception('栈空间已满')
        self.elem[self.top] = e  # 元素e压入栈顶,栈顶指针加1
        self.top += 1

    def pop(self):
        # 将栈顶元素弹出
        if self.top == self.base:
            raise Exception('栈已空')
        self.top -= 1  # 栈顶指针减1，并返回栈顶元素
        return self.elem[self.top]

    def get_top(self):
        # 返回栈顶元素
        if self.top != self.base:  # 栈非空
            return self.elem[self.top - 1]
        else:
            raise Exception('栈已空')

    def stack_empty(self):
        # 判断栈是否为空
        return self.top == self.base

    def __len__(self):
        # 栈的长度
        return self.top - self.base


def in_out_s(s, a):
    count = 0
    for i in a:
        if i == -1:
            if s.stack_empty():
                print('栈空')
            else:
                print('出栈元素是', s.pop())
        elif s.stack_size == count:
            print('栈满')
            return
        else:
            count += 1
            s.push(i)


if __name__ == "__main__":
    sq = SqStack()
    a = [int(x) for x in input().split(' ')]
    in_out_s(sq, a)
