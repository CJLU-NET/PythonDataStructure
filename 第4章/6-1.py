"""
6-1 字符统计-Python
写一个算法统计在输入字符串中各个不同字符出现的频度并将结果存入文件（字符串中的合法字符为A-Z这26个字母和0-9这10个数字）

函数接口定义：
# 统计输⼊字符串中数字字符和字⺟字符的个数
def count(ch):

@Author: FoskyM
@Date: 2023-11-03 21:24
"""

def count(ch):
    num_dict = {}
    for c in ch:
        c = c.upper()
        if c.isalnum():
            if c in num_dict:
                num_dict[c] += 1
            else:
                num_dict[c] = 1

    for i in range(10):
        if str(i) not in num_dict:
            num_dict[str(i)] = 0
        print('数字 {} 的个数= {}'.format(i, num_dict[str(i)]))

    for i in range(65, 91):
        if chr(i) not in num_dict:
            num_dict[chr(i)] = 0
        print('字⺟字符 {} 的个数= {}'.format(chr(i), num_dict[chr(i)]))


if __name__=='__main__':

    s = input()
    count(s)