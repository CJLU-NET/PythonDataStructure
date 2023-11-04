"""
6-3 自定义字符串插入函数-Python
编写算法，实现下面函数的功能。函数 insert(s, t, pos)将字符串t插入到字符串s中，插入位置为pos。假设分配给字符串s的空间足够让字符串t插入。（说明：不得使用任何库函数）

函数接口定义：
# 将字符串t插入到字符串s中，插入位置为pos
def  insert(s, t,  pos)：

@Author: FoskyM
@Date: 2023-11-04 07:56
"""

def  insert(s, t,  pos):
    if pos > len(s):
        return False
    else:
        return s[:pos-1] + t + s[pos-1:]


if __name__=='__main__':

    s = input()
    t = input()
    pos = int(input())
    if insert(s,t,pos):
        print(insert(s,t,pos))
    else:
        print('position error')