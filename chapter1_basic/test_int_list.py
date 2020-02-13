# -*- coding:utf-8 -*-
# @Author: IQer.AC
# @Date: 2020-02-11 21:57:43
# @Last Modified by:   IQer.AC
# @Last Modified time: 2020-02-11 21:57:43


class IntNode:
    __slots__ = ['item', 'next']

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class IntList(object):
    __slots__ = ['first']

    def __init__(self, item=None):
        if item:
            self.first = IntNode(item)

    def add_last(self, item):
        p = self.first
        while p.next is not None:
            p = p.next
        p.next = IntNode(item)

    def add_item(self, m, item):
        p = self.first
        while p.next and m != 0:
            print('%s->' % p.item)
            p = p.next
            m -= 1
        p.next = IntNode(item, p.next)

    def print(self):
        p = self.first
        while p.next:
            print('%s->' % p.item, end='')
            p = p.next
        print(p.item)

    def reverse(self, m, n):
        p = self.first
        while m != 0:
            print('%s->' % p.item, end='')
            p = p.next
            m -= 1
            n -= 1
        demo_list = list()
        while n >= 0:
            demo_list.append(p.item)
            p = p.next
            n -= 1
        while demo_list:
            if not p and len(demo_list) == 1:
                break
            print('%s->' % demo_list.pop(), end='')

        if p:
            while p.next:
                print('%s->' % p.item, end='')
                p = p.next
            print('%s' % p.item)


add_items = input().split(' ')
m, n = input().split(' ')
l1 = IntList(add_items.pop(0))
for i in range(len(add_items)):
    l1.add_last(add_items[i])

l1.add_item(int(m), int(n))
l1.print()
# l1.reverse(int(m), int(n))
