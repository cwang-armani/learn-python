# coding:utf-8
'''双向链表出增加和删除功能均可以继承单链表'''
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList():
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
        return count

    def travel(self):
        """链表遍历"""
        # cur 移动遍历节点 self._head指向node
        cur = self.__head
        # count计数
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表遍历"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """链表遍历"""
        # pos从零开始，小于零默认头插法
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while True:
                count += 1
                cur = cur.next
                if count == pos - 1:
                    node.next = cur.next
                    node.prev = cur
                    cur.next.prev = cur
                    cur.next = node
                    break

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """链表遍历"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()

    ll.remove(200)
    ll.travel()