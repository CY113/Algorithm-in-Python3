#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 17:44
# @Author  : Tian Hao
# @Email   : hao.tian@intcolon.cn
# @File    : 2. 栈.py
# @Software: PyCharm
# @Desc    : 栈结构
"""
1. 什么是栈？
    定义：一种有次序的数据项集合，在栈中，数据项的加入和移除都仅发生在同一端，加入/移除的端为栈顶，无操作的另一端为栈底
    举例：压子弹，堆盘子

2. 栈的特性
    - 距离栈底越近的数据项，留在栈中的时间就越长
    - 最新加入栈的数据结构被最先移除，这种次序通常称为"后进先出 LIFO(Last In First Out)"

3. 抽象数据类型：栈
    Stack() ： 创建一个空栈，不包含任何数据项
    push(item) ： 加入栈顶
    pop() ： 讲栈顶数据移除并返回
    peak() : 返回栈顶数据，无修改
    isEmpty() : 栈是否为空
    size() : 栈中数据项数量

4. 栈的应用

"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push("a")
    s.push(2)
    print(s.peek())
    print(s.pop())
    print(s.peek())
