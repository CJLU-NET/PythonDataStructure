"""
6-4 二叉排序树III-Python
已知二叉树T的结点形式为（lling,data,count,rlink），在树中查找值为X的结点，若找到，则记数（count）加1，否则，作为一个新结点插入树中，插入后仍为二叉排序树，写出其非递归算法。

函数接口定义：
在这里描述函数接口。例如：
    def search_bst(self, target):

输入样例：
在这里给出一组输入。例如：
    5
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
    7

输出样例：
在这里给出相应的输出。例如：
    1.count=0
    3.count=0
    4.count=0
    5.count=0
    6.count=0
    7.count=1
    9.count=0

@Author: FoskyM
@Date: 2023-12-21 21:58
"""

class BinaryTree:

    def __init__(self, data=None):
        self.data = data  # 数据域 data 默认为 None，data 为 None 时表示⼀颗空树
        self.lchild = None
        self.rchild = None
        self.count = 0

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
            if self.lchild is not None: self.lchild.in_order_traverse()  # 中序遍历左子树
            print(self.data + '.count=' + str(self.count))  # 访问根结点
            if self.rchild is not None: self.rchild.in_order_traverse()  # 中序遍历右子树

    def search_bst(self, target):
        p = self
        while p.data is not None:
            if target == p.data:
                p.count += 1
                break
            q = p
            if target < p.data:
                p = p.lchild
            else:
                p = p.rchild
        if p.data is None:
            s = BinaryTree(target)
            if target < q.data:
                q.lchild = s
            else:
                q.rchild = s



##请在这里填写答案

if __name__ == '__main__':
    bt = BinaryTree()
    bt.create_bitree()

    x = input()
    bt.search_bst(x)

    bt.in_order_traverse()