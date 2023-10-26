"""
6-8 双向循环队列-Python
如果允许在循环队列的两端都可以进⾏插⼊和删除操作。要求： ① 写出循环队列的类型定义； ② 写出“从队尾删除”和“从队头插⼊”的算法。

函数接口定义：
class CirQueue:

    def __init__(self, max_volume=5):

    def enqueue(self, e): # ⼊队

    def dequeue(self): # 出队

    def enqueue_from_head(self, e):

    def dequeue_from_tail(self):

@author: FoskyM
@date: 2023/10/26 09:50
"""

class CirQueue:

    def __init__(self, max_volume=5):
        self.max_volume = max_volume
        self.Q = [None] * self.max_volume
        self.front = 0
        self.rear = 0

    def enqueue(self, e): # ⼊队
        self.Q[self.front] = e
        self.front = (self.front + 1) % self.max_volume

    def dequeue(self): # 出队
        e = self.Q[self.rear]
        self.rear = (self.rear + 1) % self.max_volume
        return e

    def enqueue_from_head(self, e):
        self.rear = self.rear - 1
        self.Q[self.rear] = e

    def dequeue_from_tail(self):
        self.front = self.front - 1
        e = self.Q[self.front]
        return e


if __name__ == "__main__":

    cq = CirQueue()

    st = input().split()
    n = len(st)

    for i in range(n):
        cq.enqueue(st[i])
    for i in range(n):
        print(cq.dequeue_from_tail())

    for i in range(n):
        cq.enqueue_from_head(st[i])
    for i in range(n):
        print(cq.dequeue())