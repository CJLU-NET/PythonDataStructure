"""
6-10 单链表的递归运算-Python
已知 f 为单链表的表头指针，链表中存储的都是整型数据，试写出实现下列运算的递归算法：① 求链表中的最⼤整数； ② 求链表的结点个数； ③ 求所有整数的平均值。

函数接口定义：
### 出题人能不能长点心，函数接口定义啥也没写，还得看代码

def max_integer(f): # 求链表中的最⼤整数
def node_number(f): # 求链表的结点个数
def avg(f): # 求所有整数的平均值

@author: FoskyM
@date: 2023/10/26 10:53
"""


class LNode:

    def __init__(self, data=None):
        self.data = data  # 结点的数据域
        self.next = None  # 结点的指针域

    def __str__(self):
        return str(self.data)


class LinkList:

    def __init__(self):
        # 生成新结点作为头结点并初始化指针域和数据区域为None，头指针head指向头节点
        self.head = LNode(None)

    def create_list_r(self, l_data: list):
        # 后插法，根据l_data数据列表创建链表
        r = self.head  # 尾指针r指向头结点
        for data in l_data:
            p = LNode(data)  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            r = r.next  # r指向新的尾结点p


def max_integer(f):  # 求链表中的最⼤整数
    max_val = f.data
    f = f.next
    while f is not None:
        max_val = f.data if f.data > max_val else max_val
        f = f.next
    return max_val


def node_number(f):  # 求链表的结点个数
    count = 0
    while f is not None:
        count += 1
        f = f.next
    return count


def avg(f):  # 求所有整数的平均值
    sum = 0
    count = node_number(f)
    while f is not None:
        sum += f.data
        f = f.next
    return sum / count


if __name__ == "__main__":
    la = LinkList()

    st = [int(x) for x in input().split()]

    la.create_list_r(st)

    print(max_integer(la.head.next))
    print(node_number(la.head.next))
    print(avg(la.head.next))
