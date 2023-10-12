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
                print(p.data, end=' ')

def difference(la, lb):
    pa = la.head.next
    pb = lb.head.next
    lc = LinkList()
    lc.head.next = None
    r = lc.head

    n = 0

    while pa is not None and pb is not None:
        if pa.data < pb.data:
            r.next = pa
            r = pa
            pa = pa.next
            n += 1
        elif pa.data == pb.data:
            pa = pa.next
            pb = pb.next
        else:
            pb = pb.next

    while pa is not None:
        r.next = pa
        r = pa
        pa = pa.next
        n += 1

    r.next = None
    return lc, n



if __name__ == "__main__":
    la = LinkList()
    lb = LinkList()

    a = input()
    d1 = [int(x) for x in a.split()]
    a = input()
    d2 = [int(x) for x in a.split()]

    la.create_list_r(d1)
    lb.create_list_r(d2)
    lc, n = difference(la, lb)

    print(n)
    lc.show()