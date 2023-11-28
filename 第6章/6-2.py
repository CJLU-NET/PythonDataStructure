"""
6-2 图的基本操作（邻接表）-Python

以邻接表作为存储结构，实现以下图的基本操作：
① 增加⼀个新顶点 v，insert_vex()；
② 删除顶点 v 及其相关的边，delete_vex()；
③ 增加⼀条边<v, w>，insert_arc()；
④ 删除⼀条边<v, w>，delete_arc()。

在这里描述函数接口。例如：
def insert_vex(self, v):
def delete_vex(self, v):
def insert_arc(self, v, w):
def delete_arc(self, v, w):

输入样例：
在这里给出一组输入。例如：

5
4
A
B
C
D
E
A
B
B
C
C
D
D
E
输出样例：
在这里给出相应的输出。例如：

5个顶点4条边的初始图
A->1
B->2->0
C->3->1
D->4->2
E->3
删除顶点E
A->1
B->2->0
C->3->1
D->2
增加顶点E
A->1
B->2->0
C->3->1
D->2
E
增加边AC
A->2->1
B->2->0
C->0->3->1
D->2
E
删除边AC
A->1
B->2->0
C->3->1
D->2
E


@Author: FoskyM
@Date: 2023-11-27 21:45
"""

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

    def insert_vex(self, v):
        vertex = VNode(v)
        self.vertices.append(vertex)
        self.vexnum += 1
    def delete_vex(self, v):
        i = self.locate_vex(v)
        self.vertices.pop(i)
        self.vexnum -= 1
        for j in range(self.vexnum):
            p = self.vertices[j].firstarc
            if p is not None:
                if p.adjvex == i:
                    self.vertices[j].firstarc = p.nextarc
                else:
                    while p.nextarc is not None:
                        if p.nextarc.adjvex == i:
                            p.nextarc = p.nextarc.nextarc
                            break
                        p = p.nextarc

    def insert_arc(self, v, w):
        i = self.locate_vex(v)
        j = self.locate_vex(w)
        p1 = ArcNode()
        p1.adjvex = j
        p1.nextarc = self.vertices[i].firstarc
        self.vertices[i].firstarc = p1
        p2 = ArcNode()
        p2.adjvex = i
        p2.nextarc = self.vertices[j].firstarc
        self.vertices[j].firstarc = p2

    def delete_arc(self, v, w):
        i = self.locate_vex(v)
        j = self.locate_vex(w)
        p = self.vertices[i].firstarc
        if p.adjvex == j:
            self.vertices[i].firstarc = p.nextarc
        else:
            while p.nextarc is not None:
                if p.nextarc.adjvex == j:
                    p.nextarc = p.nextarc.nextarc
                    break
                p = p.nextarc
        p = self.vertices[j].firstarc
        if p.adjvex == i:
            self.vertices[j].firstarc = p.nextarc
        else:
            while p.nextarc is not None:
                if p.nextarc.adjvex == i:
                    p.nextarc = p.nextarc.nextarc
                    break
                p = p.nextarc

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


if __name__ == '__main__':
    g = ALGraph()
    g.create_udg()
    print(str(g.vexnum) + '个顶点' + str(g.arcnum) + '条边的初始图')
    g.show()
    g.delete_vex('E')
    print('删除顶点E')
    g.show()
    g.insert_vex('E')
    print('增加顶点E')
    g.show()
    print('增加边AC')
    g.insert_arc('A', 'C')
    g.show()
    print('删除边AC')
    g.delete_arc('A', 'C')
    g.show()
