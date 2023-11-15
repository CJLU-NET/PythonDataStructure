"""
6-5 计算二叉树最大宽度-Python

以二叉链表为存储结构，计算二叉树的最大宽度（二叉树的最大宽度是指二叉树所有层中结点个数的最大值）。

函数接口定义：
def width(self):

@Author: FoskyM
@Date: 2023-11-14 15:51
"""

max_size = 100


class SqQueue:

    def __init__(self):
        # 初始化一个空队列
        self.elem = [None] * max_size  # 为队列分配一个最大容量为max_size的数组空间
        self.front, self.rear = 0, 0  # 头指针和尾指针置为零，队列为空
        self.max_size = max_size

    def __len__(self):
        # 返回队列的元素个数，即队列的长度
        return (self.rear - self.front + self.max_size) % self.max_size

    def queue_empty(self):
        return self.front == self.rear

    def en_queue(self, e):
        # 把元素e加入队尾
        if (self.rear + 1) % self.max_size == self.front:
            # 尾指针在循环意义上加1后等于头指针，表明队满
            raise Exception('队列已满')
        self.elem[self.rear] = e  # 新元素插入队尾
        self.rear = (self.rear + 1) % self.max_size  # 队尾指针加1

    def de_queue(self):
        # 删除队头元素并将其返回
        if self.front == self.rear:  # 队空
            raise Exception('队列已空')
        e = self.elem[self.front]  # 保存队头元素
        self.front = (self.front + 1) % self.max_size  # 队头指针加1
        return e

    def get_head(self):
        # 返回队头元素，不修改队头指针
        if self.front != self.rear:  # 队列非空
            return self.elem[self.front]  # 返回队头元素的值，队头指针不变
        else:
            raise Exception('队列已空')


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

    def width(self):
        # 计算二叉树的最大宽度
        if self.data is None:
            return 0

        queue = SqQueue()
        queue.en_queue(self)
        maxw = 1
        while not queue.queue_empty():
            maxw = max(maxw, len(queue))
            for i in range(len(queue)):
                q = queue.de_queue()
                if q.lchild.data is not None:
                    queue.en_queue(q.lchild)
                if q.rchild.data is not None:
                    queue.en_queue(q.rchild)

        return maxw



if __name__ == '__main__':
    root = BinaryTree()
    root.create_bitree()

    print(root.width())