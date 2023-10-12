# 6-9 双循环链表节点换序-Python
#
# 已知 p 指向双向循环链表中的⼀个结点，其结点结构为 data、prior、next 三个域，写出 算法 change(p)，交换 p 所指向的结点及其前驱结点的顺序。
#
# 函数接口定义：
#   def exchange(self, p):

class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None


class LinkList:
    def __init__(self):
        self.head = LNode(None)
        self.head.next = self.head
        self.head.prior = self.head

    def list_insert_dul(self, i, e):
        # 在第i个位置插入节点e

        j = 0
        p = self.head
        while p.next is not self.head and j < i:
            i = i + 1
            p = p.next

        s = LNode(e)  # 生成新结点s,并将数据域置为e
        s.prior = p  # 将结点s插入双向链表中，此步对应图2.20①
        s.next = p.next  # 对应图2.20②
        p.next = s  # 对应图2.20③
        if s.next is not self.head:
            s.next.prior = s  # 对应图2.20④
        return
        raise Exception('位置不合法')

    def show(self):
        p = self.head
        while p.next is not self.head:
            print(p.next.data, end=' ')
            p = p.next

    # 请在这里填写答案 ，注意输入函数定义时需缩进4格
    def exchange(self, p):
        q = p.prior

        q.next = p.next
        q.prior.next = p
        q.prior = p

        p.prior = q.prior
        p.next.prior = q
        p.next = q


if __name__ == "__main__":

    la = LinkList()

    no = int(input())

    a = input()
    d1 = [int(x) for x in a.split()]
    for i in range(len(d1)):
        la.list_insert_dul(i, d1[i])

    p = la.head
    for i in range(no):
        p = p.next

    if p.prior is not la.head and p.next is not la.head:
        la.exchange(p)
    la.show()