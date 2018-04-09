# coding:utf-8
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        # 新元素默认指向none, next默认指向链表下一个值
        self.next = None# 新元素默认指向none

class SingleCycleLinkList(object):
    """单向链表,注意self.__head的指向"""
    def __init__(self):
        # 表头指向的位置
        node = None
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表是否为空"""
        # cur 移动遍历节点
        cur = self.__head
        # count计数
        if self.is_empty():
            return 0
        # 列表不为空进行遍历
        count = 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return  count + 1

    def travel(self):
        """链表遍历"""
        if self.is_empty():
            return  "the list is Null"
        # cur 移动遍历节点 self._head指向node
        cur = self.__head
        # count计数
        while cur.next != self.__head:
            print(cur.elem,end=" ")
            cur = cur.next
        # 退出循环后，尾节点元素未打印
        print(cur.elem, end=" ")
        print("\n")

    def add(self,item):
        """链表遍历"""
        node = Node(item)
        # 判断是否为空列表
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 先找尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环后游标处于尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self,item):
        """链表遍历"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self,pos,item):
        """链表遍历"""
        # pos从零开始，小于零默认头插法
        # 跟单链表一样的 不涉及尾部的东西
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
        # 链表是否为空
        if self.is_empty():
            return "the list is empty"
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 头节点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    rear.next = cur.next
                    self.__head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环处于尾节点，未经处理
        if cur.elem == item:
            # 只有一个节点
            if cur == self.__head:
                  self.__head = None
            # 尾节点的处理方法
            else:
                pre.next = self.__head

    def search(self,item):
        """链表遍历"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环后，尾节点元素未打印
        if cur.elem == item:
            return True
        else:
            return False

if __name__ == "__main__":

    li = SingleCycleLinkList()
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
    li.travel()
    li.insert(5,10)
    li.insert(2,20)
    li.travel()
    print(li.length())
    li.remove(5)
    li.travel()
