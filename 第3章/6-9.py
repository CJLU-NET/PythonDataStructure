"""
6-9 Ackermann函数计算-Python
已知 Ackermann 函数定义如下：
ack(m, n) = n + 1, m = 0
ack(m, n) = ack(m - 1, 1), m ≠ 0, n = 0
ack(m, n) = ack(m - 1, ack(m, n - 1)), m ≠ 0, n ≠ 0

函数接口定义：
def ack(m, n): # ackermann 函数递归
def ackermann(m, n): # ackermann 函数⾮递归

@author: FoskyM
@date: 2023/10/26 10:03
"""


def ack(m, n):  # ackermann 函数递归
    if m == 0:
        return n + 1
    elif m != 0 and n == 0:
        return ack(m - 1, 1)
    elif m != 0 and n != 0:
        return ack(m - 1, ack(m, n - 1))


def ackermann(m, n):  # ackermann 函数⾮递归
    stack = []
    while True:
        if m == 0:
            n = n + 1
            if len(stack) == 0:
                return n
            else:
                m = stack.pop()
        elif m != 0 and n == 0:
            m = m - 1
            n = 1
        elif m != 0 and n != 0:
            stack.append(m - 1)
            n = n - 1


"""
非递归的栈有点没看懂
拿 GPT 生成了另一段代码，看着蛮对的，但跑起来是错的，没细究

def ackermann(m, n):
    stack = []
    stack.append((m, n))

    while stack:
        m, n = stack.pop()

        if m == 0:
            n = n + 1
            if not stack:
                return n
        elif m != 0 and n == 0:
            stack.append((m - 1, 1))
        elif m != 0 and n != 0:
            stack.append((m - 1, n))
            stack.append((m, n - 1))
"""

if __name__ == "__main__":
    m, n = (int(x) for x in input().split(' '))
    print(ack(m, n))
    print(ackermann(m, n))
