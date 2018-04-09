# coding:utf-8
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        # 新元素默认指向none, next默认指向链表下一个值
        self.next = None# 新元素默认指向none

class SingleLinkList(object):
    """链表,注意self.__head的指向"""
    def __init__(self):
        # 表头指向的位置
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表是否为空"""
        # cur 移动遍历节点
        cur = self.__head
        # count计数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return  count

    def travel(self):
        """链表遍历"""
        # cur 移动遍历节点 self._head指向node
        cur = self.__head
        # count计数
        while cur is not None:
            print(cur.elem,end=" ")
            cur = cur.next
        print("\n")

    def add(self,item):
        """链表遍历"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """链表遍历"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """链表遍历"""
        # pos从零开始，小于零默认头插法
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            count = 0
            pre = self.__head
            while True:
                count += 1
                pre = pre.next
                if count == pos-1:
                    node.next = pre.next
                    pre.next = node
                    break

    def remove(self,item):
        """链表遍历，"""
        cur = self.__head
        pre = None
        while True:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        """链表遍历"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return  False

if __name__ == "__main__":

    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())

    li.append(1)
    print(li.is_empty())
    print(li.length())

    li.append(2)
    li.add(66)
    li.append(3)
    li.append(4)
    li.append(5)
    li.insert(5,10)
    li.insert(2,20)
    li.travel()
    print(li.length())
    li.remove(20)
    li.travel()
