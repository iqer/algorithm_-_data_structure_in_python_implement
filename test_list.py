# -*- coding:utf-8 -*- 
# @Author: IQer.AC 
# @Date: 2020-02-12 23:12:30 
# @Last Modified by:   IQer.AC 
# @Last Modified time: 2020-02-12 23:12:30 


class IntNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next


class IntList(object):

    def __init__(self, item=None):
        if item:
            self.first = IntNode(item, None)
    
    def 