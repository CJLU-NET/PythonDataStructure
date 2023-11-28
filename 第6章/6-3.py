"""
6-3 深度优先遍历-非递归-邻接表-Python

一个连通图采用邻接表作为存储结构，设计一个算法，实现从顶点v出发的深度优先遍历的非递归过程。

函数接口定义：
def dfs(self, V):

输入样例：
在这里给出一组输入。例如：

5
6
A
B
C
D
E
A
B
A
C
B
D
B
E
C
D
C
E
输出样例：
在这里给出相应的输出。例如：

5个顶点6条边的初始图
A->2->1
B->4->3->0
C->4->3->0
D->2->1
E->2->1
ABDCE

@Author: FoskyM
@Date: 2023-11-28 19:11
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


class ArcNode:  # 边结点
    def __init__(self):
        self.adjvex = 0  # 该边所指向的顶点的位置
        self.nextarc = None  # 指向下一条边的指针
        self.info = None  # 和边相关的信息


class VNode:  # 顶点信息
    def __init__(self, data):
        self.data = data  # 顶点信息
        self.firstarc = None  # 指向第一条依附该顶点的边的指针


class ALGraph:  # 邻接表
    def __init__(self):
        self.vertices = []
        self.vexnum = 0  # 图当前的顶点数
        self.arcnum = 0  # 图当前的边数

    def locate_vex(self, data):
        # 定位顶点在顶点数组中的下标
        for i in range(0, self.vexnum):
            if self.vertices[i].data == data:
                return i

    def create_udg(self):
        # 采用邻接表表示法，创建无向图
        self.vexnum = int(input())  # 输入总顶点数
        self.arcnum = int(input())  # 输入总边数
        for i in range(0, self.vexnum):  # 输入各点，构造表头结点表
            vdata = input()  # 输入顶点值
            vertex = VNode(vdata)
            self.vertices.append(vertex)
        for k in range(0, self.arcnum):  # 输入各边，构造邻接表
            v1 = input()
            v2 = input()  # 输入一条边依附的两个顶点
            i = self.locate_vex(v1)
            j = self.locate_vex(v2)  # 确定v1和v2在self中位置，即顶点在self.vertices中的序号
            p1 = ArcNode()  # 生成一个新的边结点p1
            p1.adjvex = j  # 邻接点序号为j
            p1.nextarc = self.vertices[i].firstarc
            self.vertices[i].firstarc = p1  # 将新结点p1插入顶点v1的边表头部
            p2 = ArcNode()  # 生成另一个对称的新的边结点p2
            p2.adjvex = i  # 邻接点序号为i
            p2.nextarc = self.vertices[j].firstarc
            self.vertices[j].firstarc = p2  # 将新结点p1插入顶点v1的边表头部

    def show(self):
        for i in range(0, self.vexnum):
            t = self.vertices[i]
            p = t.firstarc
            if p is None:
                print(self.vertices[i].data)
            else:
                print(t.data, end="")
                while p is not None:
                    print("->", end="")
                    print(p.adjvex, end="")
                    p = p.nextarc
                print()

    def dfs(self, V):
        visited = [False] * self.vexnum
        stack = SqStack()

        i = self.locate_vex(V)
        stack.push(i)

        while not stack.stack_empty():
            top = stack.pop()
            if not visited[top]:
                print(self.vertices[top].data, end="")
                visited[top] = True

            p = self.vertices[top].firstarc

            while p:
                if not visited[p.adjvex]:
                    stack.push(p.adjvex)
                p = p.nextarc

if __name__ == '__main__':
    g = ALGraph()
    g.create_udg()
    print(str(g.vexnum) + '个顶点' + str(g.arcnum) + '条边的初始图')
    g.show()
    g.dfs('A')