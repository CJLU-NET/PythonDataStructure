"""
6-6 循环链表表示队列-Python
假设以带头结点的循环链表表示队列，并且只设⼀个指针指向队尾元素结点（注意：不设头指针），试编写相应的置空队列、判断队列是否为空、⼊队和出队等算法。

函数接口定义：
class LinkQueue:
    def __init__(self): # ⽣成新结点作为头结点并初始化指针域和数据区域为 None，头指针 head 指向头结点

    def enqueue(self, e): # ⼊队

    def dequeue(self): # 出队

    def empty(self):

@author: FoskyM
@date: 2023/10/25 23:04
"""


class LNode:
    def __init__(self, data=None):
        self.data = data  # 结点的数据域
        self.next = None  # 结点的指针域

    def __str__(self):
        return str(self.data)

class LinkQueue:
    def __init__(self): # ⽣成新结点作为头结点并初始化指针域和数据区域为 None，头指针 head 指向头结点
        self.head = LNode()
        self.pointer = self.head

    def enqueue(self, e): # ⼊队
        node = LNode(e)
        self.pointer.next = self.pointer = node
        node.next = self.head

    def dequeue(self): # 出队
        if self.empty():
            raise Exception('队列为空')
        node = self.head.next
        self.head.next = node.next
        return node.data

    def empty(self):
        return self.head.next is None

if __name__ == "__main__":

    lq = LinkQueue()

    st = input().split()
    n = len(st)

    for i in range(n):
        lq.enqueue(st[i])

    for i in range(n):
        print(lq.dequeue())


