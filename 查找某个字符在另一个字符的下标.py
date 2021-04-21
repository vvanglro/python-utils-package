# -*- coding: UTF-8 -*-
"""
@author:wanghao
@file:查找指定字符串索引.py
@time:2021/04/04
"""


def to_find(var1, var2):
    '''
    :param var1: 待查找的字符
    :param var2: 完整的字符串
    :return:
    '''
    index= []

    var1_len = len(var1)

    szm = var1[0]

    for k in range(len(var2)):
        # 匹配首字母, 在根据首字母所在的下标位置加上var1的长度 推算判断是否和要找的字符相等
        if var2[k] == szm:
            e = var1_len + k
            # 根据推算出的起止下标开判断是否和要找的一样
            if var2[k:e] == var1:
                d = {}
                d['start'] = k
                d['end'] = e
                index.append(d)
    if not index:
        return f'Not found {var1}'

    return index



def func(var1,var2):
    import re
    r = re.finditer(var1,var2)
    print(r)
    for i in r:
        print(i.start(),i.end())

if __name__ == '__main__':
    var1 = 'to'

    var2 = 'This is a sample sentence to search for include help to search all occurrences'

    print(to_find(var1, var2))
    print(func(var1,var2))
