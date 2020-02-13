# -*- coding:utf-8 -*- 
# @Author: IQer.AC 
# @Date: 2020-02-13 10:28:30 
# @Last Modified by:   IQer.AC 
# @Last Modified time: 2020-02-13 10:28:30 


class IntNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next


class IntList(object):

    def __init__(self, item=None):
        if item:
            self.first = IntNode(item, None)
        else:
            self.first = None

    def add_last(self, item):
        if self.first:
            p = self.first
        else:
            self.first = IntNode(item, None)
            p = self.first
            return
        prev = 'first'
        while p.next:
            prev = p
            p = p.next
        if p.item[0] == 'm' and item[0] == 'f' and p.item[1] == item[1]:
            if prev == 'first':
                self.first = None
                return
            else:
                prev.next = None
            return
        p.next = IntNode(item, None)

    def pop(self):
        p = self.first
        prev = p
        while p.next:
            prev = p
            p = p.next
        prev.next = None
        return p

    def is_success(self):
        if self.first:
            return False
        else:
            return True


l1 = IntList()
i = input().split(' ')
if len(i) > 200000:
    print(False)
for item in i:
    l1.add_last(item)

print(l1.is_success())
