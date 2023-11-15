"""
6-7 二叉树的最长路径-Python

以二叉链表为存储结构，求二叉树中第一条最长路径的长度，并输出此路径上各点的值。

函数接口定义：
def longest_path(self):

@Author: FoskyM
@Date: 2023-11-15 13:54
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


class BinaryTree:

    def __init__(self, data=None):
        self.data = data  # 数据域data默认为None，data为None时表示一颗空树
        self.lchild = None
        self.rchild = None

    def create_bitree(self):
        # 按先序次序输入二叉树中结点的值（一个字符），创建二叉链表表示的二叉树
        ch = input()
        if ch == '#':  # 递归结束，建空树
            self.data = None
        else:  # 递归创建二叉树
            self.data = ch  # 根结点的数据域赋值为ch
            self.lchild = BinaryTree()  # 为当前结点创建一个空的左子树
            self.lchild.create_bitree()  # 递归创建左子树
            self.rchild = BinaryTree()  # 为当前结点创建一个空的右子树
            self.rchild.create_bitree()  # 递归创建右子树

    def in_order_traverse(self):
        # 中序遍历二叉树的递归算法
        if self.data is not None:  # 若二叉树非空
            self.lchild.in_order_traverse()  # 中序遍历左子树
            print(self.data, end=' ')  # 访问根结点
            self.rchild.in_order_traverse()  # 中序遍历右子树

    def in_order_traverse_nonre(self):
        # 中序遍历二叉树的非递归算法
        stack = []
        p = self
        while p.data is not None or stack:
            if p.data is not None:  # p非空
                stack.append(p)  # 根指针进栈
                p = p.lchild  # 根指针进栈，遍历左子树
            else:  # p为空
                q = stack.pop()  # 退栈
                print(q.data)  # 访问根结点
                p = q.rchild  # 遍历右子树

    def longest_path(self):
        ln = 0
        st = SqStack()
        if self.data is None:
            return ln, st
        else:
            ln += 1
            st.push(self)
            ln_l, st_l = self.lchild.longest_path()
            ln_r, st_r = self.rchild.longest_path()
            if ln_l > ln_r:
                ln += ln_l
                st_l_reserve = SqStack()
                while not st_l.stack_empty():
                    st_l_reserve.push(st_l.pop())
                while not st_l_reserve.stack_empty():
                    st.push(st_l_reserve.pop())
            else:
                ln += ln_r
                st_r_reserve = SqStack()
                while not st_r.stack_empty():
                    st_r_reserve.push(st_r.pop())
                while not st_r_reserve.stack_empty():
                    st.push(st_r_reserve.pop())
            return ln, st



if __name__ == '__main__':

    root = BinaryTree()
    root.create_bitree()
    # ln是最长路径的长度，st是一个栈，保存最长路径中各点的值。
    ln, st = root.longest_path()

    print(ln)
    print('最⻓路径为：')
    while not st.stack_empty():
        if (st.get_top().data is not None):
            print(st.get_top().data, end=' ')
        st.pop()