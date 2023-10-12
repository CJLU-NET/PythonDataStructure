max_size = 100


class SqList:
    def __init__(self):
        self.elem = [None] * max_size  # 为顺序表分配一个大小为max_size的数组空间
        self.length = 0  # 空表长度为0

    def list_insert(self, i, e):
        # 在顺序表中第i个位置插入新的元素e，i值的合法范围是1≤i≤self.length+1

        if i > len(self.elem):  # 存储空间已满
            raise Exception('空间已满')

        if i < 1 or i > self.length + 1:
            raise Exception('位置不合法')

        for idx in range(self.length - 1, i - 2, -1):
            self.elem[idx + 1] = self.elem[idx]  # 插入位置及之后的元素后移
        self.elem[i - 1] = e  # 将新元素e放入第i个位置
        self.length += 1  # 表长加1

    def clear_list(self):
        self.length = 0

    def list_empty(self):
        return self.length == 0

    def get_elem(self, i):
        # 返回顺序表self中的第i个元素
        if 1 <= i <= self.length:
            return self.elem[i - 1]
        raise Exception('位置不合法')

    def locate_elem(self, e):
        # 在顺序表中查找值为e的数据元素，返回其序号
        for i, elem in enumerate(self.elem[:self.length]):
            if elem == e:
                return i + 1  # 查找成功，返回序号i+1
        raise Exception('元素不存在')

    def list_delete(self, i):
        # 删除顺序表中第i个元素
        if i < 1 or i > self.length:
            raise Exception('位置不合法')
        for idx in range(i, self.length):
            self.elem[idx - 1] = self.elem[idx]  # 被删除元素之后的元素前移
        self.length -= 1  # 表长减1

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.elem[:self.length])

    def show(self):
        for i in range(self.length):
            print(self.elem[i], end=' ')

def delete_item(a, item):
    i = 0
    while i < a.length:
        if a.elem[i] == item:
            a.list_delete(i + 1)
        else:
            i += 1
    return a

if __name__ == "__main__":

    la = SqList()

    no = int(input())

    a = input()
    d1 = [int(x) for x in a.split()]
    for i in range(len(d1)):
        la.list_insert(i + 1, d1[i])

    la = delete_item(la, no)

    la.show()