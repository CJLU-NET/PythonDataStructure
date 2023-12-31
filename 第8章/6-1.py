"""
6-1 简单选择排序-单链表-Python
试以单链表为存储结构，实现简单选择排序算法。

函数接口定义：
在这里描述函数接口。例如：
    def select_sort(l):

输入样例：
在这里给出一组输入。例如：
    21
    15
    34
    23
    11

输出样例：
在这里给出相应的输出。例如：
    21 15 34 23 11
    11 15 21 23 34

@Author: FoskyM
@Date: 2023-12-31 13:57
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

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p
            p = p.next

    def __str__(self):
        output = ''
        for idx, item in enumerate(self):
            output += '{arrow}{data}'.format(arrow=' --> ' if idx else '', data=item.data)
        return output

    def __len__(self):
        cnt = 0
        for p in self:
            cnt += 1
        return cnt - 1

    def get_elem(self, i):
        # 在带头结点的单链表中根据序号i获取元素的值
        for idx, item in enumerate(self):  # 遍历链表
            if idx == i:  # 当下标加1等于i时，返回该数据元素
                return item
        raise Exception('位置不合法')

    def locate_elem(self, e):
        # 单链表的按值查找，查找成功返回第一个符合的元素，查找失败返回None
        for p in self:  # 遍历当前链表
            if p.data == e:
                return p  # 当p的值等于e, 返回p
        return None  # 未找到返回None

    def list_insert(self, i, e):
        # 在带头结点的单链表中第i个位置插入值为e的新结点
        for idx, p in enumerate(self):  # 遍历链表
            if idx + 1 == i:
                s = LNode(e)  # 生成新结点s并将s的数据域设置为e
                s.next = p.next  # 将结点s的指针域指向结点ai
                p.next = s  # 将结点p的指针域指向结点s
                return
        raise Exception('位置不合法')

    def list_delete(self, i):
        # 删除单链表中的第i个结点
        for idx, p in enumerate(self):  # 查找第i−1个结点，p指向该结点
            if idx + 1 == i and p.next is not None:
                p.next = p.next.next  # 改变删除结点前驱结点的指针域
                return
        raise Exception('位置不合法')

    def create_list_h(self, l_data: list):
        # 前插法，根据l_data数据列表创建链表
        for data in l_data:
            p = LNode(data)  # 生成新结点p，并将p结点的数据域赋值为data
            p.next = self.head.next  # 将新结点p插入到头结点之后
            self.head.next = p

    def create_list_r(self, l_data: list):
        # 后插法，根据l_data数据列表创建链表
        r = self.head  # 尾指针r指向头结点
        for data in l_data:
            p = LNode(data)  # 生成新结点，并初始化p的数据域为data
            r.next = p  # 将新结点p插入尾结点r之后
            r = r.next  # r指向新的尾结点p

    def show(self):
        for x in self:
            if x.data is not None: print(x.data, end=' ')
        print(end='\n')


def select_sort(l):
    p = l.head.next
    while p is not None:
        min = p
        q = p.next
        while q is not None:
            if q.data < min.data:
                min = q
            q = q.next
        if min is not p:
            p.data, min.data = min.data, p.data
        p = p.next


# 以下方法链表的插入和删除操作都需要遍历链表，所以时间复杂度为O(n^2)

# def select_sort(l):
#     length = len(l) + 1
#     for i in range(1, length):
#         min = i
#         for j in range(i + 1, length):
#             if l.get_elem(j).data < l.get_elem(min).data:
#                 min = j
#         tmp1 = l.get_elem(i).data
#         tmp2 = l.get_elem(min).data
#         l.list_delete(i)
#         l.list_insert(i, tmp2)
#         l.list_delete(min)
#         l.list_insert(min, tmp1)


if __name__ == '__main__':

    data = []
    for i in range(5):
        data.append(int(input()))

    l = LinkList()
    l.create_list_r(data)

    l.show()
    select_sort(l)
    l.show()
