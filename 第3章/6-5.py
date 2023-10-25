"""
6-5 判断进出栈序列是否合法-Python
假设以 I 和 O 分别表示⼊栈和出栈操作。栈的初态和终态均为空，⼊栈和出栈的操作序 列可表示为仅由 I 和 O 组成的序列，称可以操作的序列为合法序列，否则称为⾮法序列。

函数接口定义：
    def check(seq):

@author: FoskyM
@date: 2023/10/25 22:23
"""

max_size = 100


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

def check(seq):
    stack = SqStack()
    for s in seq:
        if s == 'I':
            stack.push(s)
        elif s == 'O':
            if stack.stack_empty():
                return False
            else:
                stack.pop()
        else:
            return False
    if stack.stack_empty():
        return True

    return False

if __name__ == "__main__":

    st = input()
    if check(st):
        print(st, " is a legal sequence")
    else:
        print(st, " is a illegal sequence")