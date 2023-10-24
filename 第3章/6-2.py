"""
6-2 回文判断-Python
回⽂是指正读反读均相同的字符序列，如“abba”和“abdba”均是回⽂，但“good”不是回⽂。 试写⼀个算法判定给定的字符序列是否为回⽂。（提示：将⼀半字符⼊栈）
函数接口定义：
    在这里描述函数接口。例如：
    def is_palindrome(t):

@Author: FoskyM
@Date: 2023-10-24 22:50
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


def is_palindrome(t):
    stack = SqStack()
    i = 0
    for i in range(len(t) // 2):
        stack.push(t[i])

    i += 1

    if len(t) % 2 == 1:
        i += 1

    while i < len(t):
        if stack.pop() != t[i]:
            return False
        i += 1

    return True


if __name__ == "__main__":

    st = input()
    if is_palindrome(st):
        print(st, "is a palindrome.")
    else:
        print(st, "is not a palindrome.")
