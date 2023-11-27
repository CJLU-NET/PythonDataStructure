"""
6-1 图的基本操作（邻接矩阵）-Python

以邻接矩阵作为存储结构，实现以下图的基本操作：
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
1
B
C
2
C
D
3
D
E
4
输出样例：
在这里给出相应的输出。例如：

5个顶点4条边的初始图
∞	1	∞	∞	∞
1	∞	2	∞	∞
∞	2	∞	3	∞
∞	∞	3	∞	4
∞	∞	∞	4	∞
删除顶点E
∞	1	∞	∞
1	∞	2	∞
∞	2	∞	3
∞	∞	3	∞
增加顶点E
∞	1	∞	∞	∞
1	∞	2	∞	∞
∞	2	∞	3	∞
∞	∞	3	∞	∞
∞	∞	∞	∞	∞
增加边AC
∞	1	1	∞	∞
1	∞	2	∞	∞
1	2	∞	3	∞
∞	∞	3	∞	∞
∞	∞	∞	∞	∞
删除边AC
∞	1	∞	∞	∞
1	∞	2	∞	∞
∞	2	∞	3	∞
∞	∞	3	∞	∞
∞	∞	∞	∞	∞

@Author: FoskyM
@Date: 2023-11-26 21:28
"""

INF = 0x3f3f3f3f  # 无穷大


class AMGraph:
    def __init__(self):
        self.vexs = []  # 顶点表
        self.arcs = []  # 邻接矩阵
        self.vexnum = 0  # 图的当前点数
        self.arcnum = 0  # 图的当前边数

    def locate_vex(self, name):
        # 定位顶点在顶点数组中的下标
        for i in range(0, self.vexnum):
            if self.vexs[i] == name:
                return i

    def create_udn(self):
        # 采用邻接矩阵表示法，创建无向网
        self.vexnum = int(input())  # 输入总顶点数
        self.arcnum = int(input())  # 输入总边数
        for i in range(0, self.vexnum):
            vexname = input()
            self.vexs.append(vexname)
        self.arcs = [[INF for i in range(self.vexnum)] for i in range(self.vexnum)]  # 初始化邻接矩阵，边的权值均置为无穷大
        for k in range(0, self.arcnum):  # 构造邻接矩阵
            v1 = input()
            v2 = input()
            w = int(input())  # 输入一条边依附的顶点及权值
            i = self.locate_vex(v1)
            j = self.locate_vex(v2)  # 确定v1和v2在图中的位置，即顶点数组的下标
            self.arcs[i][j] = w  # 边<v1,v2>的权值为w
            self.arcs[j][i] = self.arcs[i][j]  # 置<v1,v2>的对称边<v2,v1>的权值为w

    def insert_vex(self, v):
        self.vexs.append(v)
        self.vexnum += 1
        for i in range(self.vexnum - 1):
            self.arcs[i].append(INF)
        self.arcs.append([INF for i in range(self.vexnum)])

    def delete_vex(self, v):
        i = self.locate_vex(v)
        #self.vexs.pop(i)
        self.vexnum -= 1
        self.arcs.pop(i)
        for j in range(self.vexnum):
            self.arcs[j].pop(i)

    def insert_arc(self, v, w):
        self.arcnum += 1
        i = self.locate_vex(v)
        j = self.locate_vex(w)
        self.arcs[i][j] = 1
        self.arcs[j][i] = self.arcs[i][j]

    def delete_arc(self, v, w):
        self.arcnum -= 1
        i = self.locate_vex(v)
        j = self.locate_vex(w)
        self.arcs[i][j] = INF
        self.arcs[j][i] = self.arcs[i][j]

    def show(self):
        for i in range(0, self.vexnum):
            for j in range(0, self.vexnum):
                if j != self.vexnum - 1:
                    if (self.arcs[i][j] < INF):
                        print(self.arcs[i][j], end="\t")
                    else:
                        print("∞\t", end="")
                else:
                    if (self.arcs[i][j] < INF):
                        print(self.arcs[i][j])
                    else:
                        print("∞")


if __name__ == '__main__':
    g = AMGraph()
    g.create_udn()
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
