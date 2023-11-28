"""
6-6 路径测试2-邻接表-Python
采用邻接表存储结构，编写一个算法，判别无向图中任意给定的两个顶点之间是否存在一条长度为为k的简单路径。

函数接口定义：
在这里描述函数接口。例如：
def path_lenk(self, i, j, k):
# 判断邻接表⽅式存储的有向图 g 的顶点 i 到 j 是否存在⻓度为 k 的简单路径

输入样例：
在这里给出一组输入。例如：

4
4
A
B
C
D
A
B
B
C
C
D
D
A
A
D
3
输出样例：
在这里给出相应的输出。例如：

4个顶点4条边的初始图
A->3->1
B->2->0
C->3->1
D->0->2
分别输入两个顶点和路径长度
顶点A和顶点D有长度为3的路径

@Author: FoskyM
@Date: 2023-11-28 22:48
"""

visited = []  # 访问标志数组，其初值为"false"
for m in range(0, 100):
    visited.append(False)  # 访问标志数组初始化


class ArcNode:  # 边结点
    def __init__(self):
        self.adjvex = None  # 该边所指向的顶点的位置
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
        # 采用邻接表表示法，创建有向图
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

    def path_lenk(self, i, j, k):
        if k == 0:
            if i == j:
                return True
            else:
                return False
        else:
            visited[i] = True
            p = self.vertices[i].firstarc
            while p is not None:
                if not visited[p.adjvex]:
                    if self.path_lenk(p.adjvex, j, k - 1):
                        return True
                p = p.nextarc
            visited[i] = False
            return False


if __name__ == '__main__':

    g = ALGraph()
    g.create_udg()
    print(str(g.vexnum) + '个顶点' + str(g.arcnum) + '条边的初始图')
    g.show()
    print('分别输入两个顶点和路径长度')
    a = input()
    b = input()
    k = int(input())
    i = g.locate_vex(a)
    j = g.locate_vex(b)
    if g.path_lenk(i, j, k):
        print('顶点' + a + '和顶点' + b + '有长度为' + str(k) + '的路径')
    else:
        print('顶点' + a + '和顶点' + b + '没有长度为' + str(k) + '的路径')