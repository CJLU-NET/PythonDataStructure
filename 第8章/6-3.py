"""
6-3 快排式查找-Python
借助于快速排序的算法思想，在一组无序的记录中查找给定关键字值等于key的记录。设此组记录存放于数组r[l..n]中。若查找成功，则输出该记录在r数组中的位置及其值，否则显示“not find”信息。

函数接口定义：
在这里描述函数接口。例如：
    def search(r, low, high, key):
    # 在数组 r[low..high]中查找关键字值等于 key 的记录

输入样例：
在这里给出一组输入。例如：
    1 2 3 4 9 8 7 6 5
    9

输出样例：
在这里给出相应的输出。例如：
    [1, 2, 3, 4, 9, 8, 7, 6, 5]
    data[4]= 9

@Author: FoskyM
@Date: 2023-12-31 14:23
"""


def search(r, low, high, key):
    while low < high:
        if r[low] > key > r[high]:
            high -= 1
            low += 1
        while low <= high and r[high] > key:
            high -= 1
        if r[high] == key:
            return high
        while low <= high and r[low] < key:
            low += 1
        if r[low] == key:
            return low
        return -1


if __name__ == '__main__':

    data = [int(x) for x in input().split(' ')]
    print(data)

    x = int(input())
    result = search(data, 0, len(data) - 1, x)
    if result == -1:
        print("Not find")  # 查找失败
    else:
        print('data[' + str(result) + ']=', data[result])
