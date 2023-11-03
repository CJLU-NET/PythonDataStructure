"""
6-2 字符串逆序存储-Python
写一个递归算法来实现字符串逆序存储，要求不另设串存储空间。

函数接口定义：
# 递归实现字符串的逆序存储
def inverse(ch):

@Author: FoskyM
@Date: 2023-11-03 22:07
"""

def inverse(ch):
    if len(ch) == 1:
        return ch
    else:
        return inverse(ch[1:]) + ch[0]


if __name__=='__main__':

    s = input()
    print(inverse(s))