# 6-7 链表逆置-Python
#
# 设计⼀个算法，将链表中所有结点的链接⽅向“原地”逆转，即要求仅利⽤原表的存储空 间，换句话说，要求算法的空间复杂度为 O(1)。
#
# 函数接口定义：
# def inverse(la):

class LNode:
    def __init__(self, data=None):
        self.data = data  # 结点的数据域
        self.next = None  # 结点的指针域

class LinkList:
    def __init__(self):
        # 生成新结点作为头结点并初始化指针域和数据区域为None，头指针head指向头节点
        self.head = LNode(None)

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def create_list_r(self, l_data: list):
        # 后插法，根据l_data数据列表创建链表
        r = self.head  # 尾指针r指向头结点
        for data in l_data:
            p = LNode(data)  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            r = r.next  # r指向新的尾结点p
    def show(self):
        for p in self:
            if p.data is not None:
                print(p.data,end=' ')

def inverse(la):
    p = la.head.next
    la.head.next = None
    while p is not None:
        q = p
        p = p.next
        q.next = la.head.next
        la.head.next = q
    return la

# def inverse(la):
#     lb = LinkList()
#     lb.head.next = None
#
#     pa = la.head.next
#
#     while pa is not None:
#         q = pa
#         pa = pa.next
#         q.next = lb.head.next
#         lb.head.next = q
#
#     return lb

if __name__ == "__main__":

    la=LinkList()

    a = input()
    d1 = [int(x) for x in a.split()]
    la.create_list_r(d1)

    la=inverse(la)
    la.show()