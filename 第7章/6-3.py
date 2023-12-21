"""
6-3 二叉排序树II-Python
已知二叉排序树采用二叉链表存储结构，根结点的指针为T，链结点的结构为（lchild,data,rchild），其中lchild，rchild分别指向该结点左、右孩子的指针，data域存放结点的数据信息。请写出递归算法，从小到大输出二叉排序树中所有数据值>=x的结点的数据。要求先找到第一个满足条件的结点后，再依次输出其他满足条件的结点。


函数接口定义：
在这里描述函数接口。例如：
    def search_bst(self, x):

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
    1

输出样例：
在这里给出相应的输出。例如：
    1
    3
    4
    5
    6
    7
    9

@Author: FoskyM
@Date: 2023-12-21 21:33
"""


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

    def search_bst(self, x):
        if self.data is None:
            return
        if self.data >= x:
            self.lchild.search_bst(x)
            print(self.data)
            self.rchild.search_bst(x)
        else:
            self.rchild.search_bst(x)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.create_bitree()

    x = input()
    bt.search_bst(x)
