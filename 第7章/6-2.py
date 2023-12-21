"""
6-2 二叉排序树-Python

函数接口定义：
在这里描述函数接口。例如：
    def judge_bst(self):

输入样例：
在这里给出一组输入。例如：
    3
    1
    #
    #
    4
    #
    #
    7
    6
    #
    #
    9
    #
    #

输出样例：
在这里给出相应的输出。例如：
    Yes

@Author: FoskyM
@Date: 2023-12-21 20:27
"""

pre = None


class BinaryTree:

    def __init__(self, data=None):
        self.data = data  # 数据域 data 默认为 None，data 为 None 时表示⼀颗空树
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

    def judge_bst(self):
        global pre
        if self.data is None:
            return True
        if not self.lchild.judge_bst():
            return False
        if pre is not None and self.data <= pre.data:
            return False
        pre = self
        if not self.rchild.judge_bst():
            return False
        return True


if __name__ == '__main__':

    bt = BinaryTree()
    bt.create_bitree()

    if bt.judge_bst():
        print("Yes")
    else:
        print("No")