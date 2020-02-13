# -*- coding:utf-8 -*-
# @Author: IQer.AC
# @Date: 2020-02-10 22:08:42
# @Last Modified by:   IQer.AC
# @Last Modified time: 2020-02-10 22:08:42


class IntNode(object):

    def __init__(self, i, n):
        self.item = i
        self.next = n


class SLList(object):
    def __init__(self, x=None):
        if x:
            self.__first = IntNode(x, None)
            self.__size = 1
        else:
            self.__size = 0

    def add_first(self, x):
        self.__first = IntNode(x, self.first)
        self.size += 1

    def get_first(self):
        return self.first.item

    def add_last(self, x):
        p = self.__first
        while p.next is not None:
            p = p.next
        p.next = IntNode(x, None)
        self.__size += 1

    def __size(self):
        # if p.next is None:
        #     return 1
        # else:
        #     return 1 + self.__size(p.next)
        return self.__size

    def reverse(self):
        self.

    # def size(self):
    #     return self.__size(self.__first)


l1 = SLList(5)
l1.add_first(10)
l1.add_first(15)

# print(l1.size())

# print(l1.first)
# print(l1.rest.first)
# print(l1.rest.rest.first)

items = input().split(' ')
sum = int(input())

if len(items) > 25:
    print(False)
elif len(items) != len(set(items)):
    print(False)
else:
    items.sort()
    s = 0
    for i in items:
        s += int(i)
        if s == sum:
            print(True)
            break
        elif s > sum:
            print(False)
            break
    else:
        print(False)
