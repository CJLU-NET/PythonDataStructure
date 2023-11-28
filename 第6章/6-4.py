"""
6-4 距给定顶点距离最远的点-邻接矩阵-Python
设计一个算法，求图G中距离顶点v的最短路径长度最大的一个顶点，设v可达其余各个顶点。

函数接口定义：
在这里描述函数接口。例如：
def shortest_path_max(self, V):

输入样例：
在这里给出一组输入。例如：

6
10
A
B
C
D
E
F
A
B
6
A
C
1
A
D
5
B
C
5
B
E
3
C
D
5
C
E
6
C
F
4
D
F
2
E
F
6
输出样例：
在这里给出相应的输出。例如：

6个顶点10条边的初始图
∞	6	1	5	∞	∞
6	∞	5	∞	3	∞
1	5	∞	5	6	4
5	∞	5	∞	∞	2
∞	3	6	∞	∞	6
∞	∞	4	2	6	∞
距离顶点A最短距离最长的顶点是 E

@Author: FoskyM
@Date: 2023-11-28 22:16
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

    def shortest_path_max(self, V):
        v = self.locate_vex(V)
        dist = [INF for i in range(self.vexnum)]
        dist[v] = 0
        for i in range(self.vexnum):
            if i != v:
                dist[i] = self.arcs[v][i]
        for k in range(self.vexnum):
            for i in range(self.vexnum):
                for j in range(self.vexnum):
                    if dist[i] > dist[j] + self.arcs[j][i]:
                        dist[i] = dist[j] + self.arcs[j][i]
        max = 0
        for i in range(self.vexnum):
            if dist[i] > max:
                max = dist[i]
                j = i
        return j


if __name__ == '__main__':
    g = AMGraph()
    g.create_udn()
    print(str(g.vexnum) + '个顶点' + str(g.arcnum) + '条边的初始图')
    g.show()
    print('距离顶点A最短距离最长的顶点是', g.vexs[g.shortest_path_max('A')])