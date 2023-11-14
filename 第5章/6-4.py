"""
6-4 二叉树的双序遍历-Python

以二叉链表为存储结构，设计算法实现二叉树的双序遍历（双序遍历是指对二叉树的每个结点，先访问这个结点，然后按双序遍历它的左子树，然后再一次访问这个结点，接下来按双序遍历它的右子树）。

函数接口定义：
def double_traverse(self):

@Author: FoskyM
@Date: 2023-11-14 15:36
"""

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

    def double_traverse(self):
        if self.data is None:
            return

        print(self.data, end=' ')
        self.lchild.double_traverse()
        print(self.data, end=' ')
        self.rchild.double_traverse()


if __name__ == '__main__':
    root = BinaryTree()
    root.create_bitree()

    root.double_traverse()