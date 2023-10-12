# 6-8 链表的条件删除-Python
#
# 设计⼀个算法，删除递增有序链表中值⼤于 mink 且⼩于 maxk 的所有元素（mink 和 maxk 是给定的两个参数，其值可以和表中的元素相同，也可以不同）。
#
# 函数接口定义：
# def delete_min_max(la, mink, maxk):

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


def delete_min_max(la, mink, maxk):
    pa = la.head
    while pa.next is not None:
        if mink < pa.next.data < maxk:
            pa.next = pa.next.next
        else:
            pa = pa.next
    return la


if __name__ == "__main__":
    la = LinkList()

    a = input()
    mink, maxk = (int(x) for x in a.split())
    a = input()
    d1 = [int(x) for x in a.split()]
    la.create_list_r(d1)

    la = delete_min_max(la, mink, maxk)
    la.show()
