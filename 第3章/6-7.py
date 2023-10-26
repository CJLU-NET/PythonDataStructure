"""
6-7 带标志的循环队列-Python
假设以数组 Q[m]存放循环队列中的元素，同时设置⼀个标志 tag，以 tag == 0 和 tag == 1 来区别在队头指针（front）和队尾指针（rear）相等时，队列状态为“空”还是“满”。试编写与此结 构相应的插⼊（enqueue）和删除（dequeue）算法。

函数接口定义：
class CirQueue:
    def __init__(self, max_volume=5):

    def enqueue(self, e): # ⼊队

    def dequeue(self): # 出队

@author: FoskyM
@date: 2023/10/26 09:45
"""

class CirQueue:
    def __init__(self, max_volume=5):
        self.max_volume = max_volume
        self.Q = [None] * self.max_volume
        self.front = 0
        self.rear = 0
        self.tag = 0

    def enqueue(self, e): # ⼊队
        if self.front == self.rear and self.tag == 1:
            print("Queue is full!")
            return
        self.Q[self.rear] = e
        self.rear = (self.rear + 1) % self.max_volume
        self.tag = 1

    def dequeue(self): # 出队
        if self.front == self.rear and self.tag == 0:
            print("Queue is empty!")
            return
        e = self.Q[self.front]
        self.front = (self.front + 1) % self.max_volume
        self.tag = 0
        return e

if __name__ == "__main__":

    cq = CirQueue()

    st = input().split()
    n = len(st)

    for i in range(n):
        cq.enqueue(st[i])

    for i in range(n):
        print(cq.dequeue())