"""
6-4 计算后缀表达式的值-Python
从键盘上输⼊⼀个后缀表达式，试编写算法计算表达式的值。规定：逆波兰表达式的长度不超过一行，以$作为输⼊结束，操作数之间用空格分隔，操作符只可能有+、−、∗、/四种运 算。例如：234 34 + 2*$。

函数接口定义：
def postfix(e):

@author: FoskyM
@date: 2023/10/25 17:08
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


def postfix(e):
    stack = SqStack()

    num = ''
    for s in e:
        if s.isdigit() or s == '.':  # 一定要注意小数点，改了又改 PTA 上一直部分正确，后面想到浮点数的小数才猛然醒悟
            num += s
        else:
            if num:
                stack.push(float(num))
                num = ''

            if s == ' ':
                continue
            elif s == '$':
                break
            elif s in '+-*/':
                b = stack.pop()
                a = stack.pop()
                r = 0
                if s == '+':
                    r = a + b
                elif s == '-':
                    r = a - b
                elif s == '*':
                    r = a * b
                elif s == '/':
                    r = a / b
                stack.push(r)
    return stack.pop()


if __name__ == "__main__":
    st = input()
    val = postfix(st)
    print(val)
