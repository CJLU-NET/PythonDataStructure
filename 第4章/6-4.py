"""
6-4 字符串格式化-Python
已知字符串S1中存放一段英文，写出算法format(s1,s2,s3,n),将其按给定的长度n格式化成两端对齐的字符串S2, 其多余的字符送S3。

函数接口定义：
# 将 s1拆分成 s2和 s3，要求 s2⻓度为 n 且两端对⻬
def format(s1, s2, s3, n):

@Author: FoskyM
@Date: 2023-11-04 08:01
"""

def format(s1, s2, s3, n):
    if s1.isspace():
        return 1
    if len(s1) < n:
        return 2
    i = 0
    while i < n:
        s2.append(s1[i])
        i += 1
    i = n
    while i < len(s1):
        s3.append(s1[i])
        i += 1

    return 0

if __name__=='__main__':

    s1 = input()
    n = int(input())
    s2=[]
    s3=[]
    m = format(s1,s2,s3,n)
    if m == 0 :
        for i in s2:
            print(i,end='')
        print(end='\n')
        for i in s3:
            print(i,end='')
    elif m==1 :
        print("字符串 s1为空串或空格串")
    else:
        print("字符串 s1没有", n, "个有效字符")
